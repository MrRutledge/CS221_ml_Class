{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "ComputeEditDistance.py",
      "provenance": [],
      "authorship_tag": "ABX9TyO6YC904EKSmd2rTqUwEt19",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MrRutledge/CS221_ml_Class/blob/master/ComputeEditDistance.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4mTWtpCU5iOA",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "d18686b0-676e-4b71-de43-f403423fe734"
      },
      "source": [
        "def computeEditDistance (s, t):\n",
        "    cache  = {} # (m,n) => result \n",
        "    def recurse (m,n): \n",
        "        \"\"\"\n",
        "        Return the minimum edit distance between:\n",
        "        - first m letters of s\n",
        "        - first n letters of t \n",
        "\n",
        "        \"\"\"\n",
        "        if (m,n)  in cache:\n",
        "          return cache [(m,n)]\n",
        "        if m == 0: #base case \n",
        "            result  = n \n",
        "        elif n == 0: # base case\n",
        "            result = m \n",
        "        elif s[m-1] == t[n-1]: # last letter matches\n",
        "            result  = recurse(m-1, n-1)\n",
        "        else:\n",
        "            subCost = 1 + recurse(m-1, n-1)\n",
        "            delCost = 1 + recurse(m-1, n)\n",
        "            insCost = 1 + recurse(m, n-1)\n",
        "            result  = min(subCost, delCost, insCost)\n",
        "        cache[(m,n)] = result \n",
        "        return result\n",
        "\n",
        "    return recurse(len(s), len(t))\n",
        "\n",
        "#print(computeEditDistance('a cat', 'the cats'))\n",
        "print(computeEditDistance(' cow'* 10, 'cows '))\n",
        "\n"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "36\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NGIR6T1d9UVw",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}