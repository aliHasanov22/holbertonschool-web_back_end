# Caching

This project is part of the Python backend curriculum and focuses on implementing different caching systems in Python. The goal is to understand how caches work, why they are useful, and how different cache replacement policies behave when the cache becomes full.

## Project Description

A cache is a temporary storage area used to keep frequently accessed data so it can be retrieved faster. Since cache memory is limited, a caching system needs rules to decide which item to remove when new data must be added.

In this project, different caching strategies are implemented by creating classes that inherit from a common parent class, `BaseCaching`.

## Learning Objectives

By the end of this project, you should be able to explain:

- What a caching system is
- What the purpose of a caching system is
- What limits a caching system has
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All files are interpreted/compiled on Ubuntu 20.04 LTS using Python 3.9
- All files must end with a new line
- The first line of all files must be exactly:

```python
#!/usr/bin/env python3
