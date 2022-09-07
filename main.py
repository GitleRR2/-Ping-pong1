        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        if ball.rect.x > win_width:
            finish = True
            window(lose2, (200, 200))
            game_over = True

        racket1.reset()
        racket1.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)