# Google-Foobar

Here you can find my solutions for Google Foobar.

![Google Foobar Screenshot](https://user-images.githubusercontent.com/22143882/98168224-8eafd280-1eea-11eb-84d0-a4e53eee7840.png)

[Google Foobar](http://foobar.withgoogle.com) is Google's secret recruiting process embedded within their search engine. There are 5 levels, each with a different number of challenges that follow a story.

Checkout [journal.md](https://github.com/maikka39/Google-Foobar/blob/master/journal.md) for the overall story with each level.

Inside each level is a challenge folder with a problem file describing the challenge and constraints, and my solution to the challenge.

## Levels

### Level 1

- [Prison Labor Dodgers](https://github.com/maikka39/Google-Foobar/tree/master/Level%201/Prison%20Labor%20Dodgers)

### Level 2

- [Bunny Prisoner Locating](https://github.com/maikka39/Google-Foobar/tree/master/Level%202/Bunny%20Prisoner%20Locating)
- [En Route Salute](https://github.com/maikka39/Google-Foobar/tree/master/Level%202/En%20Route%20Salute)

### Level 3

- [Bomb, Baby!](https://github.com/maikka39/Google-Foobar/tree/master/Level%203/Bomb%20Baby)
- [Doomsday Fuel](https://github.com/maikka39/Google-Foobar/tree/master/Level%203/Doomsday%20Fuel)
- [Prepare The Bunnies' Escape](https://github.com/maikka39/Google-Foobar/tree/master/Level%203/Prepare%20The%20Bunnies%20Escape)

At this point, I was offered to send my solutions to a Google recruiter. Checkout the [questionnaire.md](https://github.com/maikka39/Google-Foobar/blob/master/Level%203/questionnaire.md) for details.

### Level 4

- [Running with Bunnies](https://github.com/maikka39/Google-Foobar/tree/master/Level%204/Running%20with%20Bunnies)
- [Bringing a Gun to a Trainer Fight](https://github.com/maikka39/Google-Foobar/tree/master/Level%204/Bringing%20a%20Gun%20to%20a%20Trainer%20Fight)

### Level 5

- [Disorderly Escape](https://github.com/maikka39/Google-Foobar/tree/master/Level%205/Disorderly%20Escape)

## End

In the end it showed me a rabbit animation and I got an encrypted message:

```xml
<encrypted>
FkYaHggCVkoeRklRS0ZUSwgAHUxHQRRaAg0FDgoGRlxKQVNLTARATQgEBA4PRh8ZSgQPDQQTR0pK QVNLTAhdWh8EDQIJDVYeQUFOCggJWlwbBAQOBRUUGVdBTh4FDVxaBgQNTEdBFEsMAwsCHxIUGVdB ThgKB1YeQUFODQQOFBlXQU4cAg8SHhA= 
</encrypted>
```

It looks `base64` encoded but when we decode it we just get garbage data. Then I saw the little hint below:

> For **your** eyes only!

And as it turns out, you just have to decrypt the output from the `base64` decoded string using a simple `xor` with your username.

I did this easily using [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)XOR(%7B'option':'UTF8','string':'maikka39'%7D,'Standard',false)&input=RmtZYUhnZ0NWa29lUmtsUlMwWlVTd2dBSFV4SFFSUmFBZzBGRGdvR1JseEtRVk5MVEFSQVRRZ0VCQTRQUmg4WlNnUVBEUVFUUjBwSyBRVk5MVEFoZFdoOEVEUUlKRFZZZVFVRk9DZ2dKV2x3YkJBUU9CUlVVR1ZkQlRoNEZEVnhhQmdRTlRFZEJGRXNNQXdzQ0h4SVVHVmRCIFRoZ0tCMVllUVVGT0RRUU9GQmxYUVU0Y0FnOFNIaEE9).

This gave me the following output:

```js
{'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}
```
