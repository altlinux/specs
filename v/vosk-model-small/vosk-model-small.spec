%global voskdir %_datadir/vosk-api
%global voskmodeldir %voskdir/models

Name: vosk-model-small
Version: 1.0.0
Release: alt1

Summary: Collection of small language models for vosk-api
License: Apache-2.0
Group: Development/Databases
Url: https://alphacephei.com/vosk/models

Source: %name-%version.tar

BuildRequires: rpm-build-python3

BuildArch: noarch

%description
%summary

%package en-us
Summary: Lightweight model for the US English language
Group: Development/Databases

%description en-us
%summary.

%package en-in
Summary: Lightweight model for the Indian English language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description en-in
%summary.

%package cn
Summary: Lightweight model for the Chinese language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description cn
%summary.

%package ru
Summary: Lightweight model for the Russian language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description ru
%summary.

%package fr
Summary: Lightweight model for the French language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description fr
%summary.

%package de
Summary: Lightweight model for the German language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description de
%summary.

%package es
Summary: Lightweight model for the Spanish language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description es
%summary.

%package pt
Summary: Lightweight model for the Portuguese language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description pt
%summary.

%package tr
Summary: Lightweight model for the Turksih language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description tr
%summary.

%package vn
Summary: Lightweight model for the Vietnamese language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description vn
%summary.

%package it
Summary: Lightweight model for the Italian language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description it
%summary.

%package nl
Summary: Lightweight model for the Dutch language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description nl
%summary.

%package ca
Summary: Lightweight model for the Catalan language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description ca
%summary.

%package fa
Summary: Lightweight model for the Farsi (Persian) language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description fa
%summary.

%package kz
Summary: Lightweight model for the Kazakh language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description kz
%summary.

%package ja
Summary: Lightweight model for the Japanese language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description ja
%summary.

%package hi
Summary: Lightweight model for the Hindi language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description hi
%summary.

%package pl
Summary: Lightweight model for the Polish language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description pl
%summary.

%package uz
Summary: Lightweight model for the Uzbek language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description uz
%summary.

%package ko
Summary: Lightweight model for the Korean language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description ko
%summary.

%package gu
Summary: Lightweight model for the Gujarati language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description gu
%summary.

%package tg
Summary: Lightweight model for the Tajik language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description tg
%summary.

%package te
Summary: Lightweight model for the Telugu language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description te
%summary.

%package ky
Summary: Lightweight model for the Kyrgyz language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description ky
%summary.

%package ka
Summary: Lightweight model for the Georgian language
Group: Development/Databases
Requires: %name
%filter_from_requires /vosk/d

%description ka
%summary.

%prep
%setup

%install
mkdir -p %buildroot%voskmodeldir
cp -rv vosk-model-small-en-us-0.15 %buildroot%voskmodeldir/vosk-model-small-en-us
cp -rv vosk-model-small-en-in-0.4 %buildroot%voskmodeldir/vosk-model-small-en-in
cp -rv vosk-model-small-cn-0.22 %buildroot%voskmodeldir/vosk-model-small-cn
cp -rv vosk-model-small-ru-0.22 %buildroot%voskmodeldir/vosk-model-small-ru
cp -rv vosk-model-small-fr-0.22 %buildroot%voskmodeldir/vosk-model-small-fr
cp -rv vosk-model-small-de-0.15 %buildroot%voskmodeldir/vosk-model-small-de
cp -rv vosk-model-small-es-0.42 %buildroot%voskmodeldir/vosk-model-small-es
cp -rv vosk-model-small-pt-0.3 %buildroot%voskmodeldir/vosk-model-small-pt
cp -rv vosk-model-small-tr-0.3 %buildroot%voskmodeldir/vosk-model-small-tr
cp -rv vosk-model-small-vn-0.4 %buildroot%voskmodeldir/vosk-model-small-vn
cp -rv vosk-model-small-it-0.22 %buildroot%voskmodeldir/vosk-model-small-it
cp -rv vosk-model-small-nl-0.22 %buildroot%voskmodeldir/vosk-model-small-nl
cp -rv vosk-model-small-ca-0.4 %buildroot%voskmodeldir/vosk-model-small-ca
cp -rv vosk-model-small-fa-0.42 %buildroot%voskmodeldir/vosk-model-small-fa
cp -rv vosk-model-small-kz-0.42 %buildroot%voskmodeldir/vosk-model-small-kz
cp -rv vosk-model-small-ja-0.22 %buildroot%voskmodeldir/vosk-model-small-ja
cp -rv vosk-model-small-hi-0.22 %buildroot%voskmodeldir/vosk-model-small-hi
cp -rv vosk-model-small-pl-0.22 %buildroot%voskmodeldir/vosk-model-small-pl
cp -rv vosk-model-small-uz-0.22 %buildroot%voskmodeldir/vosk-model-small-uz
cp -rv vosk-model-small-ko-0.22 %buildroot%voskmodeldir/vosk-model-small-ko
cp -rv vosk-model-small-gu-0.42 %buildroot%voskmodeldir/vosk-model-small-gu
cp -rv vosk-model-small-tg-0.22 %buildroot%voskmodeldir/vosk-model-small-tg
cp -rv vosk-model-small-te-0.42 %buildroot%voskmodeldir/vosk-model-small-te
cp -rv vosk-model-small-ky-0.42 %buildroot%voskmodeldir/vosk-model-small-ky
cp -rv vosk-model-small-ka-0.42 %buildroot%voskmodeldir/vosk-model-small-ka

%files
%dir %voskdir
%dir %voskmodeldir

%files en-us
%voskmodeldir/vosk-model-small-en-us

%files en-in
%voskmodeldir/vosk-model-small-en-in

%files cn
%voskmodeldir/vosk-model-small-cn

%files ru
%voskmodeldir/vosk-model-small-ru

%files fr
%voskmodeldir/vosk-model-small-fr

%files de
%voskmodeldir/vosk-model-small-de

%files es
%voskmodeldir/vosk-model-small-es

%files pt
%voskmodeldir/vosk-model-small-pt

%files tr
%voskmodeldir/vosk-model-small-tr

%files vn
%voskmodeldir/vosk-model-small-vn

%files it
%voskmodeldir/vosk-model-small-it

%files nl
%voskmodeldir/vosk-model-small-nl

%files ca
%voskmodeldir/vosk-model-small-ca

%files fa
%voskmodeldir/vosk-model-small-fa

%files kz
%voskmodeldir/vosk-model-small-kz

%files ja
%voskmodeldir/vosk-model-small-ja

%files hi
%voskmodeldir/vosk-model-small-hi

%files pl
%voskmodeldir/vosk-model-small-pl

%files uz
%voskmodeldir/vosk-model-small-uz

%files ko
%voskmodeldir/vosk-model-small-ko

%files gu
%voskmodeldir/vosk-model-small-gu

%files tg
%voskmodeldir/vosk-model-small-tg

%files te
%voskmodeldir/vosk-model-small-te

%files ky
%voskmodeldir/vosk-model-small-ky

%files ka
%voskmodeldir/vosk-model-small-ka

%changelog
* Mon May 25 2026 Ulysses Apokin <ulysses@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus:
  + vosk-model-small-en-us 0.15
  + vosk-model-small-en-in 0.4
  + vosk-model-small-cn 0.22
  + vosk-model-small-ru 0.22
  + vosk-model-small-fr 0.22
  + vosk-model-small-de 0.15
  + vosk-model-small-es 0.42
  + vosk-model-small-pt 0.3
  + vosk-model-small-tr 0.3
  + vosk-model-small-vn 0.4
  + vosk-model-small-it 0.22
  + vosk-model-small-nl 0.22
  + vosk-model-small-ca 0.4
  + vosk-model-small-fa 0.42
  + vosk-model-small-kz 0.42
  + vosk-model-small-ja 0.22
  + vosk-model-small-hi 0.22
  + vosk-model-small-pl 0.22
  + vosk-model-small-uz 0.22
  + vosk-model-small-ko 0.22
  + vosk-model-small-gu 0.42
  + vosk-model-small-tg 0.22
  + vosk-model-small-te 0.42
  + vosk-model-small-ky 0.42
  + vosk-model-small-ka 0.42
