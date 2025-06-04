from django.shortcuts import render
from .forms import PGNUploadForm
import chess.pgn
import chess.engine

def analyze_pgn(request):
    context = {}
        if request.method == 'POST':
                form = PGNUploadForm(request.POST, request.FILES)
                        if form.is_valid():
                                    pgn_file = request.FILES['pgn_file']
                                                game = chess.pgn.read_game(pgn_file)
                                                            board = game.board()

                                                                        engine = chess.engine.SimpleEngine.popen_uci("/workspaces/chess-analyzer/stockfish/stockfish")  # ← adapte le chemin !

                                                                                    analysis = []
                                                                                                for move in game.mainline_moves():
                                                                                                                board.push(move)
                                                                                                                                info = engine.analyse(board, chess.engine.Limit(time=0.1))
                                                                                                                                                score = info['score'].relative
                                                                                                                                                                analysis.append((move.uci(), str(score)))

                                                                                                                                                                            engine.quit()
                                                                                                                                                                                        context['analysis'] = analysis
                                                                                                                                                                                            else:
                                                                                                                                                                                                    form = PGNUploadForm()

                                                                                                                                                                                                        context['form'] = form
                                                                                                                                                                                                            return render(request, 'analysis/analyze.html', context)