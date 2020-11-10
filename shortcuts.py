import forms
import app
import models
from flask import (Flask, g, render_template, flash, redirect, url_for)

stats = ('Goals Scored', 'Goals Conceded', 'Passes', 'Shots', 'Fouls', 'Possession')


def create_shortcut():
    for x in stats:
        print(stats)
