import pygame as pg


def sword_handle_locator(img, mx, my):
    img_rect = img.get_rect(center=(mx, my))
    handle_x = img_rect.centerx
    handle_y = img_rect.centery
    return handle_x, handle_y



