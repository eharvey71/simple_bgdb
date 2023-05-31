<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-10">
                <h1>Board Games</h1>
                <hr><br><br>
                <alert :message=message v-if="showMessage"></alert>
                <button type="button" class="btn btn-success btn-sm" @click="toggleAddGameModal">
                    Add Board Game
                </button>
                <br><br>
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">Title</th>
                            <th scope="col">Designer</th>
                            <th scope="col">Publisher</th>
                            <th scope="col">Played?</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(game, index) in games" :key="index">
                            <td>{{ game.title }}</td>
                            <td>{{ game.designer }}</td>
                            <td>{{ game.publisher }}</td>
                            <td>
                                <span v-if="game.played">Yes</span>
                                <span v-else>No</span>
                            </td>
                            <td>
                                <div class="btn-group" role="group">
                                    <button type="button" class="btn btn-warning btn-sm" @click="toggleEditGameModal(game)">
                                        Update
                                    </button>
                                    <button type="button" class="btn btn-danger btn-sm"
                                        @click="handleDeleteGame(game)">Delete</button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <!-- add new game modal -->
        <div ref="addGameModal" class="modal fade" :class="{ show: activeAddGameModal, 'd-block': activeAddGameModal }"
            tabindex="-1" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Add a new game</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"
                            @click="toggleAddGameModal">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form>
                            <div class="mb-3">
                                <label for="addGameTitle" class="form-label">Title:</label>
                                <input type="text" class="form-control" id="addGameTitle" v-model="addGameForm.title"
                                    placeholder="Enter title">
                            </div>
                            <div class="mb-3">
                                <label for="addGameDesigner" class="form-label">Designer:</label>
                                <input type="text" class="form-control" id="addGameDesigner" v-model="addGameForm.designer"
                                    placeholder="Enter designer">
                            </div>
                            <div class="mb-3">
                                <label for="addGamePublisher" class="form-label">Publisher:</label>
                                <input type="text" class="form-control" id="addGamePublisher" v-model="addGameForm.publisher"
                                    placeholder="Enter publisher">
                            </div>
                            <div class="mb-3 form-check">
                                <input type="checkbox" class="form-check-input" id="addGamePlayed" v-model="addGameForm.played">
                                <label class="form-check-label" for="addGamePlayed">Played?</label>
                            </div>
                            <div class="btn-group" role="group">
                                <button type="button" class="btn btn-primary btn-sm" @click="handleAddSubmit">
                                    Submit
                                </button>
                                <button type="button" class="btn btn-danger btn-sm" @click="handleAddReset">
                                    Reset
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="activeAddGameModal" class="modal-backdrop fade show"></div>
        <!-- edit game modal -->
        <div ref="editGameModal" class="modal fade" :class="{ show: activeEditGameModal, 'd-block': activeEditGameModal }"
            tabindex="-1" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Update</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"
                            @click="toggleEditGameModal">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form>
                            <div class="mb-3">
                                <label for="editGameTitle" class="form-label">Title:</label>
                                <input type="text" class="form-control" id="editGameTitle" v-model="editGameForm.title"
                                    placeholder="Enter title">
                            </div>
                            <div class="mb-3">
                                <label for="editGameDesigner" class="form-label">Author:</label>
                                <input type="text" class="form-control" id="editGameDesigner" v-model="editGameForm.designer"
                                    placeholder="Enter designer">
                            </div>
                            <div class="mb-3">
                                <label for="editGamePublisher" class="form-label">Publisher:</label>
                                <input type="text" class="form-control" id="editGamePublisher" v-model="editGameForm.publisher"
                                    placeholder="Enter publisher">
                            </div>
                            <div class="mb-3 form-check">
                                <input type="checkbox" class="form-check-input" id="editGamePlayed"
                                    v-model="editGameForm.played">
                                <label class="form-check-label" for="editGamePlayed">Played?</label>
                            </div>
                            <div class="btn-group" role="group">
                                <button type="button" class="btn btn-primary btn-sm" @click="handleEditSubmit">
                                    Submit
                                </button>
                                <button type="button" class="btn btn-danger btn-sm" @click="handleEditCancel">
                                    Cancel
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="activeEditGameModal" class="modal-backdrop fade show"></div>
    </div>
</template>
  
<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
    data() {
        return {
            activeAddGameModal: false,
            addGameForm: {
                title: '',
                designer: '',
                publisher: '',
                played: [],
            },
            activeEditGameModal: false,
            editGameForm: {
                id: '',
                title: '',
                designer: '',
                publisher: '',
                played: [],
            },
            games: [],
            message: '',
            showMessage: false,
        };
    },
    components: {
        alert: Alert,
    },
    methods: {
        addGame(payload) {
            const path = 'http://localhost:5001/games';
            axios.post(path, payload)
                .then(() => {
                    this.getGames();
                    this.message = 'Game added!';
                    this.showMessage = true;
                })
                .catch((error) => {

                    console.log(error);
                    this.getGames();
                });
        },
        getGames() {
            const path = 'http://localhost:5001/games';
            axios.get(path)
                .then((res) => {
                    this.games = res.data.games;
                })
                .catch((error) => {

                    console.error(error);
                });
        },
        updateGame(payload, gameID) {
            const path = `http://localhost:5001/games/${gameID}`;
            axios.put(path, payload)
                .then(() => {
                    this.getGames();
                    this.message = 'Game updated!';
                    this.showMessage = true;
                })
                .catch((error) => {
                    console.error(error);
                    this.getGames();
                });
        },
        handleAddReset() {
            this.initForm();
        },
        handleAddSubmit() {
            this.toggleAddGameModal();
            let played = false;
            if (this.addGameForm.played[0]) {
                played = true;
            }
            const payload = {
                title: this.addGameForm.title,
                designer: this.addGameForm.designer,
                publisher: this.addGameForm.publisher,
                played, // property shorthand
            };
            this.addGame(payload);
            this.initForm();
        },
        handleEditSubmit() {
            this.toggleEditGameModal(null);
            let played = false;
            if (this.editGameForm.played) played = true;
            const payload = {
                title: this.editGameForm.title,
                designer: this.editGameForm.designer,
                publisher: this.editGameForm.publisher,
                read,
            };
            this.updateGame(payload, this.editGameForm.id);
        },
        handleEditCancel() {
            this.toggleEditGameModal(null);
            this.initForm();
            this.getGames(); // why?
        },
        handleDeleteGame(game) {
            this.removeGame(game.id);
        },
        removeGame(gameID) {
            const path = `http://localhost:5001/games/${gameID}`;
            axios.delete(path)
                .then(() => {
                    this.getGames();
                    this.message = 'Game removed!';
                    this.showMessage = true;
                })
                .catch((error) => {
                    console.error(error);
                    this.getGames();
                });
        },
        initForm() {
            this.addGameForm.title = '';
            this.addGameForm.designer = '';
            this.addGameForm.publisher = '';
            this.addGameForm.played = [];
            this.editGameForm.id = '';
            this.editGameForm.title = '';
            this.editGameForm.designer = '';
            this.editGameForm.publisher = '';
            this.editGameForm.played = [];
        },
        toggleAddGameModal() {
            const body = document.querySelector('body');
            this.activeAddGameModal = !this.activeAddGameModal;
            if (this.activeAddGameModal) {
                body.classList.add('modal-open');
            } else {
                body.classList.remove('modal-open');
            }
        },
        toggleEditGameModal(game) {
            if (game) {
                this.editGameForm = game;
            }
            const body = document.querySelector('body');
            this.activeEditGameModal = !this.activeEditGameModal;
            if (this.activeEditGameModal) {
                body.classList.add('modal-open');
            } else {
                body.classList.remove('modal-open');
            }
        },
    },
    created() {
        this.getGames();
    },
};
</script>