#!/usr/bin/env python

PLAYCHESS_PKG_DIR = "/home/pal/tiago_public_ws/src/playchess"
GUI_SCRIPTS_DIR   = PLAYCHESS_PKG_DIR + "/scripts/gui"

#Pieces characteristics
king = {
'name': 'king',
'diameter': 0.03, #m
'weight': 34, #g
'height': 0.085, #m
'center_height': 0.8875, #m
'gripper_closure': 'closing_for_king'
}

queen = {
'name': 'queen',
'diameter': 0.03,
'weight': 33,
'height': 0.075,
'center_height': 0.8825,
'gripper_closure': 'closing_for_queen'
}

bishop = {
'name': 'bishop',
'diameter': 0.025,
'weight': 20,
'height': 0.064,
'center_height': 0.877,
'gripper_closure': 'closing_for_bishop'
}

knight = {
'name': 'knight',
'diameter': 0.03,
'weight': 25,
'height': 0.06,
'center_height': 0.875,
'gripper_closure': 'closing_for_knight'
}

rook = {
'name': 'rook',
'diameter': 0.025,
'weight': 18,
'height': 0.046,
'center_height': 0.868,
'gripper_closure': 'closing_for_rook'
}

pawn = {
'name': 'pawn',
'diameter': 0.025,
'weight': 15,
'height': 0.04,
'center_height': 0.865,
'gripper_closure': 'closing_for_pawn'
}

#Pieces coordinates at the start of the game
pieces_coordinates = {
'rook_h1': ['h1', rook],
'knight_g1': ['g1', knight],
'bishop_f1': ['f1', bishop],
'king_e1': ['e1', king],
'queen_d1': ['d1', queen],
'bishop_c1': ['c1', bishop],
'knight_b1': ['b1', knight],
'rook_a1': ['a1', rook],
'pawn_h2': ['h2', pawn],
'pawn_g2': ['g2', pawn],
'pawn_f2': ['f2', pawn],
'pawn_e2': ['e2', pawn],
'pawn_d2': ['d2', pawn],
'pawn_c2': ['c2', pawn],
'pawn_b2': ['b2', pawn],
'pawn_a2': ['a2', pawn],
'pawn_h7': ['h7', pawn],
'pawn_g7': ['g7', pawn],
'pawn_f7': ['f7', pawn],
'pawn_e7': ['e7', pawn],
'pawn_d7': ['d7', pawn],
'pawn_c7': ['c7', pawn],
'pawn_b7': ['b7', pawn],
'pawn_a7': ['a7', pawn],
'rook_h8': ['h8', rook],
'knight_g8': ['g8', knight],
'bishop_f8': ['f8', bishop],
'king_e8': ['e8', king],
'queen_d8': ['d8', queen],
'bishop_c8': ['c8', bishop],
'knight_b8': ['b8', knight],
'rook_a8': ['a8', rook]
}

squares_to_index_white = {
'h1': 63,
'g1': 62,
'f1': 61,
'e1': 60,
'd1': 59,
'c1': 58,
'b1': 57,
'a1': 56,
'h2': 55,
'g2': 54,
'f2': 53,
'e2': 52,
'd2': 51,
'c2': 50,
'b2': 49,
'a2': 48,
'h3': 47,
'g3': 46,
'f3': 45,
'e3': 44,
'd3': 43,
'c3': 42,
'b3': 41,
'a3': 40,
'h4': 39,
'g4': 38,
'f4': 37,
'e4': 36,
'd4': 35,
'c4': 34,
'b4': 33,
'a4': 32,
'h5': 31,
'g5': 30,
'f5': 29,
'e5': 28,
'd5': 27,
'c5': 26,
'b5': 25,
'a5': 24,
'h6': 23,
'g6': 22,
'f6': 21,
'e6': 20,
'd6': 19,
'c6': 18,
'b6': 17,
'a6': 16,
'h7': 15,
'g7': 14,
'f7': 13,
'e7': 12,
'd7': 11,
'c7': 10,
'b7': 9,
'a7': 8,
'h8': 7,
'g8': 6,
'f8': 5,
'e8': 4,
'd8': 3,
'c8': 2,
'b8': 1,
'a8': 0
}

squares_to_index_black = {
'h1': 0,
'g1': 1,
'f1': 2,
'e1': 3,
'd1': 4,
'c1': 5,
'b1': 6,
'a1': 7,
'h2': 8,
'g2': 9,
'f2': 10,
'e2': 11,
'd2': 12,
'c2': 13,
'b2': 14,
'a2': 15,
'h3': 16,
'g3': 17,
'f3': 18,
'e3': 19,
'd3': 20,
'c3': 21,
'b3': 22,
'a3': 23,
'h4': 24,
'g4': 25,
'f4': 26,
'e4': 27,
'd4': 28,
'c4': 29,
'b4': 30,
'a4': 31,
'h5': 32,
'g5': 33,
'f5': 34,
'e5': 35,
'd5': 36,
'c5': 37,
'b5': 38,
'a5': 39,
'h6': 40,
'g6': 41,
'f6': 42,
'e6': 43,
'd6': 44,
'c6': 45,
'b6': 46,
'a6': 47,
'h7': 48,
'g7': 49,
'f7': 50,
'e7': 51,
'd7': 52,
'c7': 53,
'b7': 54,
'a7': 55,
'h8': 56,
'g8': 57,
'f8': 58,
'e8': 59,
'd8': 60,
'c8': 61,
'b8': 62,
'a8': 63
}


rows_white = {
'row8': [0, 1, 2, 3, 4, 5, 6, 7],
'row7': [8, 9, 10, 11, 12, 13, 14, 15],
'row6': [16, 17, 18, 19, 20, 21, 22, 23],
'row5': [24, 25, 26, 27, 28, 29, 30, 31],
'row4': [32, 33, 34, 35, 36, 37, 38, 39],
'row3': [40, 41, 42, 43, 44, 45, 46, 47],
'row2': [48, 49, 50, 51, 52, 53, 54, 55],
'row1': [56, 57, 58, 59, 60, 61, 62, 63]
}

rows_black = {
'row1': [0, 1, 2, 3, 4, 5, 6, 7],
'row2': [8, 9, 10, 11, 12, 13, 14, 15],
'row3': [16, 17, 18, 19, 20, 21, 22, 23],
'row4': [24, 25, 26, 27, 28, 29, 30, 31],
'row5': [32, 33, 34, 35, 36, 37, 38, 39],
'row6': [40, 41, 42, 43, 44, 45, 46, 47],
'row7': [48, 49, 50, 51, 52, 53, 54, 55],
'row8': [56, 57, 58, 59, 60, 61, 62, 63]
}
'''
rows_black = {
'row1': [7, 6, 5, 4, 3, 2, 1, 0],
'row2': [15, 14, 13, 12, 11, 10, 9, 8],
'row3': [23, 22, 21, 20, 19, 18, 17, 16],
'row4': [31, 30, 29, 28, 27, 26, 25, 24],
'row5': [39, 38, 37, 36, 35, 34, 33, 32],
'row6': [47, 46, 45, 44, 43, 42, 41, 40],
'row7': [55, 54, 53, 52, 51, 50, 49, 48],
'row8': [63, 62, 61, 60, 59, 58, 57, 56]
}
'''

columns = { #Columns indexes are the same for both black and white
'columnA': [56, 48, 40, 32, 24, 16, 8, 0],
'columnB': [57, 49, 41, 33, 25, 17, 9, 1],
'columnC': [58, 50, 42, 34, 26, 18, 10, 2],
'columnD': [59, 51, 43, 35, 27, 19, 11, 3],
'columnE': [60, 52, 44, 36, 28, 20, 12, 4],
'columnF': [61, 53, 45, 37, 29, 21, 13, 5],
'columnG': [62, 54, 46, 38, 30, 22, 14, 6],
'columnH': [63, 55, 47, 39, 31, 23, 15, 7]
}

columns_black = { #Columns indexes are the same for both black and white
'columnA': [63, 55, 47, 39, 31, 23, 15, 7],
'columnB': [62, 54, 46, 38, 30, 22, 14, 6],
'columnC': [61, 53, 45, 37, 29, 21, 13, 5],
'columnD': [60, 52, 44, 36, 28, 20, 12, 4],
'columnE': [59, 51, 43, 35, 27, 19, 11, 3],
'columnF': [58, 50, 42, 34, 26, 18, 10, 2],
'columnG': [57, 49, 41, 33, 25, 17, 9, 1],
'columnH': [56, 48, 40, 32, 24, 16, 8, 0]
}

columns_explicit = { #Columns indexes are the same for both black and white
'columnA': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
'columnB': ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8'],
'columnC': ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'],
'columnD': ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8'],
'columnE': ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8'],
'columnF': ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8'],
'columnG': ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8'],
'columnH': ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
}

#Live chessboard situation to keep track of the pieces movements on the chessboard. This will be updated after each move.
live_chessboard_situation = {
'h1': 'rook_h1',
'g1': 'knight_g1',
'f1': 'bishop_f1',
'e1': 'king_e1',
'd1': 'queen_d1',
'c1': 'bishop_c1',
'b1': 'knight_b1',
'a1': 'rook_a1',
'h2': 'pawn_h2',
'g2': 'pawn_g2',
'f2': 'pawn_f2',
'e2': 'pawn_e2',
'd2': 'pawn_d2',
'c2': 'pawn_c2',
'b2': 'pawn_b2',
'a2': 'pawn_a2',
'h3': 'none',
'g3': 'none',
'f3': 'none',
'e3': 'none',
'd3': 'none',
'c3': 'none',
'b3': 'none',
'a3': 'none',
'h4': 'none',
'g4': 'none',
'f4': 'none',
'e4': 'none',
'd4': 'none',
'c4': 'none',
'b4': 'none',
'a4': 'none',
'h5': 'none',
'g5': 'none',
'f5': 'none',
'e5': 'none',
'd5': 'none',
'c5': 'none',
'b5': 'none',
'a5': 'none',
'h6': 'none',
'g6': 'none',
'f6': 'none',
'e6': 'none',
'd6': 'none',
'c6': 'none',
'b6': 'none',
'a6': 'none',
'h7': 'pawn_h7',
'g7': 'pawn_g7',
'f7': 'pawn_f7',
'e7': 'pawn_e7',
'd7': 'pawn_d7',
'c7': 'pawn_c7',
'b7': 'pawn_b7',
'a7': 'pawn_a7',
'h8': 'rook_h8',
'g8': 'knight_g8',
'f8': 'bishop_f8',
'e8': 'king_e8',
'd8': 'queen_d8',
'c8': 'bishop_c8',
'b8': 'knight_b8',
'a8': 'rook_a8'
}

live_chessboard_situation_complete = {
'h1': ['none', 'none'],
'g1': ['king_e1', 'white'],
'f1': ['rook_h1', 'white'],
'e1': ['none', 'none'],
'd1': ['queen_d1', 'white'],
'c1': ['bishop_c1', 'white'],
'b1': ['knight_b1', 'white'],
'a1': ['rook_a1', 'white'],
'h2': ['pawn_h2', 'white'],
'g2': ['pawn_g2', 'white'],
'f2': ['pawn_f2', 'white'],
'e2': ['none', 'none'],
'd2': ['none', 'none'],
'c2': ['pawn_c2', 'white'],
'b2': ['pawn_b2', 'white'],
'a2': ['pawn_a2', 'white'],
'h3': ['none', 'none'],
'g3': ['none', 'none'],
'f3': ['knight_g1', 'white'],
'e3': ['none', 'none'],
'd3': ['none', 'none'],
'c3': ['none', 'none'],
'b3': ['none', 'none'],
'a3': ['none', 'none'],
'h4': ['none', 'none'],
'g4': ['none', 'none'],
'f4': ['none', 'none'],
'e4': ['pawn_e2', 'white'],
'd4': ['none', 'none'],
'c4': ['bishop_f1', 'white'],
'b4': ['none', 'none'],
'a4': ['none', 'none'],
'h5': ['none', 'none'],
'g5': ['none', 'none'],
'f5': ['none', 'none'],
'e5': ['none', 'none'],
'd5': ['none', 'none'],
'c5': ['bishop_f8', 'black'],
'b5': ['none', 'none'],
'a5': ['none', 'none'],
'h6': ['none', 'none'],
'g6': ['none', 'none'],
'f6': ['knight_g8', 'black'],
'e6': ['none', 'none'],
'd6': ['none', 'none'],
'c6': ['knight_b8', 'black'],
'b6': ['none', 'none'],
'a6': ['none', 'none'],
'h7': ['pawn_h7', 'black'],
'g7': ['pawn_g7', 'black'],
'f7': ['pawn_f7', 'black'],
'e7': ['none', 'none'],
'd7': ['none', 'none'],
'c7': ['pawn_d2', 'white'],
'b7': ['pawn_b7', 'black'],
'a7': ['pawn_a7', 'black'],
'h8': ['none', 'none'],
'g8': ['king_e8', 'black'],
'f8': ['rook_h8', 'black'],
'e8': ['none', 'none'],
'd8': ['queen_d8', 'black'],
'c8': ['bishop_c8', 'black'],
'b8': ['rook_a8', 'black'],
'a8': ['none', 'none']
}

starting_chessboard_situation_complete = {
'h1': ['rook_h1', 'white'],
'g1': ['knight_g1', 'white'],
'f1': ['bishop_f1', 'white'],
'e1': ['king_e1', 'white'],
'd1': ['queen_d1', 'white'],
'c1': ['bishop_c1', 'white'],
'b1': ['knight_b1', 'white'],
'a1': ['rook_a1', 'white'],
'h2': ['pawn_h2', 'white'],
'g2': ['pawn_g2', 'white'],
'f2': ['pawn_f2', 'white'],
'e2': ['paen_e2', 'white'],
'd2': ['pawn_d2', 'white'],
'c2': ['pawn_c2', 'white'],
'b2': ['pawn_b2', 'white'],
'a2': ['pawn_a2', 'white'],
'h3': ['none', 'none'],
'g3': ['none', 'none'],
'f3': ['none', 'none'],
'e3': ['none', 'none'],
'd3': ['none', 'none'],
'c3': ['none', 'none'],
'b3': ['none', 'none'],
'a3': ['none', 'none'],
'h4': ['none', 'none'],
'g4': ['none', 'none'],
'f4': ['none', 'none'],
'e4': ['none', 'none'],
'd4': ['none', 'none'],
'c4': ['none', 'none'],
'b4': ['none', 'none'],
'a4': ['none', 'none'],
'h5': ['none', 'none'],
'g5': ['none', 'none'],
'f5': ['none', 'none'],
'e5': ['none', 'none'],
'd5': ['none', 'none'],
'c5': ['none', 'none'],
'b5': ['none', 'none'],
'a5': ['none', 'none'],
'h6': ['none', 'none'],
'g6': ['none', 'none'],
'f6': ['none', 'none'],
'e6': ['none', 'none'],
'd6': ['none', 'none'],
'c6': ['none', 'none'],
'b6': ['none', 'none'],
'a6': ['none', 'none'],
'h7': ['pawn_h7', 'black'],
'g7': ['pawn_g7', 'black'],
'f7': ['pawn_f7', 'black'],
'e7': ['pawn_e7', 'black'],
'd7': ['pawn_d7', 'black'],
'c7': ['pawn_c7', 'black'],
'b7': ['pawn_b7', 'black'],
'a7': ['pawn_a7', 'black'],
'h8': ['rook_h8', 'black'],
'g8': ['knight_g8', 'black'],
'f8': ['bishop_f8', 'black'],
'e8': ['king_e8', 'black'],
'd8': ['queen_d8', 'black'],
'c8': ['bishop_c8', 'black'],
'b8': ['knight_b8', 'black'],
'a8': ['rook_a8', 'black']
}