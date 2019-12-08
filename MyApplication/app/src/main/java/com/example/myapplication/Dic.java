package com.example.myapplication;

import android.graphics.drawable.Drawable;
import android.media.Image;

public class Dic {
    private Drawable image;
    private String title;

    public Dic(Drawable image, String title) {
        this.image = image;
        this.title = title;
    }

    public Drawable getImage() {
        return image;
    }

    public void setImage(Drawable image) {
        this.image = image;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
}
