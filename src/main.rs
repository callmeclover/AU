use enigo::{Enigo, Key};
use rand::prelude::*;
use rand::distributions::WeightedIndex;
use rsautogui::{mouse, mouse::Speed, mouse::Button, mouse::ScrollAxis};
use std::thread;
use std::time::Duration;

fn main() {
    let jump_thread = thread::spawn(jump);
    let mouse_thread = thread::spawn(mouse);

    let mut rng = thread_rng();
    let mut enigo = Enigo::new();
    let list = [("w", 1), ("a", 1), ("s", 1), ("d", 1), ("e", 1), ("left", 1), ("right", 1), ("none", 1)];
    let index = WeightedIndex::new(list.iter().map(|item| item.1)).unwrap();
    loop {
        loop {
            match list[index.sample(&mut rng)].0 {
                "w" => {
                    enigo.key_down(Key::W);
                    thread::sleep(Duration::from_millis(rng.gen_range(100..=5000)));
                    enigo.key_up(Key::W);
                },
                "a" => {
                    enigo.key_down(Key::A);
                    thread::sleep(Duration::from_millis(rng.gen_range(100..=5000)));
                    enigo.key_up(Key::A);
                },
                "s" => {
                    enigo.key_down(Key::S);
                    thread::sleep(Duration::from_millis(rng.gen_range(100..=5000)));
                    enigo.key_up(Key::S);
                },
                "d" => {
                    enigo.key_down(Key::D);
                    thread::sleep(Duration::from_millis(rng.gen_range(100..=5000)));
                    enigo.key_up(Key::D);
                },
                "e" => {
                    enigo.key_down(Key::E);
                    thread::sleep(Duration::from_millis(rng.gen_range(100..=5000)));
                    enigo.key_up(Key::E);
                },
                "left" => {
                    enigo.key_down(Key::LeftArrow);
                    thread::sleep(Duration::from_millis(rng.gen_range(100..=5000)));
                    enigo.key_up(Key::LeftArrow);
                },
                "right" => {
                    enigo.key_down(Key::RightArrow);
                    thread::sleep(Duration::from_millis(rng.gen_range(100..=5000)));
                    enigo.key_up(Key::RightArrow);
                },
                _ => {}
            }
            thread::sleep(Duration::from_millis(rng.gen_range(100..=5000)));
        }
    }
}

fn jump() {
    let mut rng = thread_rng();
    let mut enigo = Enigo::new();
    let list = [("jump", 1), ("none", 10)];
    let index = WeightedIndex::new(list.iter().map(|item| item.1)).unwrap();
    loop {
        match list[index.sample(&mut rng)].0 {
            "jump" => {
                enigo.key_down(Key::Space);
                thread::sleep(Duration::from_millis(rng.gen_range(100..=5000)));
                enigo.key_up(Key::Space);
            },
            _ => {}
        }
        thread::sleep(Duration::from_millis(rng.gen_range(100..=5000)));
    }
}

fn mouse() {
    let mut rng = thread_rng();
    let mut enigo = Enigo.new();
    let (display_width, display_height) = enigo.main_display_size();
    let list = [("leftclick", 1), ("rightclick", 1), ("lefthold", 1), ("righthold", 1), ("leftdrag", 1), ("rightdrag", 1), ("drag", 1), ("move", 1), ("scrollx", 1), ("scrolly", 1), ("scrollxy", 1), ("none", 10)];
    let index = WeightedIndex::new(list.iter().map(|item| item.1)).unwrap();
    loop {
        match list[index.sample(&mut rng)].0 {
            "leftclick" => {
                mouse::click(Button::Left);
            },
            "rightclick" => {
                mouse::click(Button::Right);
            },
            "lefthold" => {
                mouse::down(Button::Left);
                thread::sleep(Duration::from_millis(rng.gen_range(100..=5000)));
                mouse::up(Button::Left);
            },
            "righthold" => {
                mouse::down(Button::Right);
                thread::sleep(Duration::from_millis(rng.gen_range(100..=5000)));
                mouse::up(Button::Right);
            },
            "leftdrag" => {
                mouse::down(Button::Left);
                mouse::slow_drag_rel();
                mouse::up(Button::Left);
            },
            "rightdrag" => {
                mouse::down(Button::Right);
                mouse::slow_drag_rel();
                mouse::up(Button::Right);
            },
            "drag" => {
                mouse::slow_drag_rel(rng.gen_range(0..=));
            },
            "scrollx" => {
                mouse::scroll(ScrollAxis::X, rng.gen_range(1..=10));
            },
            "scrolly" => {
                mouse::scroll(ScrollAxis::Y, rng.gen_range(1..=10));
            },
            "scrollxy" => {
                mouse::scroll(ScrollAxis::X, rng.gen_range(1..=10));
                mouse::scroll(ScrollAxis::Y, rng.gen_range(1..=10));
            },
            _ => {}
        }
        thread::sleep(Duration::from_millis(rng.gen_range(100..=5000)));
    }
}