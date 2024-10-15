%define _unpackaged_files_terminate_build 1

Name:    mbrola-voices
Version: 20200332
Release: alt1
BuildArch: noarch

Summary: Data files of mbrola speech synthesizer voices
License: AGPL-3.0-or-later
Group:   Sound
Url:     https://github.com/numediart/MBROLA-voices

Source: %name-%version.tar

#BuildRequires:

%description
%summary

%package en1
Summary: en1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola
Provides: mbrola-voice-en1 = %EVR
Obsoletes: mbrola-voice-en1: < %EVR

%description en1
%summary

%files en1
%dir %_datadir/mbrola/en1
%_datadir/mbrola/en1/*

%package us1
Summary: us1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola
Provides: mbrola-voice-us1 = %EVR
Obsoletes: mbrola-voice-us1 < %EVR

%description us1
%summary

%files us1
%dir %_datadir/mbrola/us1
%_datadir/mbrola/us1/*

%package us2
Summary: us2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola
Provides: mbrola-voice-us2 = %EVR
Obsoletes: mbrola-voice-us2 < %EVR

%description us2
%summary

%files us2
%dir %_datadir/mbrola/us2
%_datadir/mbrola/us2/*

%package us3
Summary: us3 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola
Provides: mbrola-voice-us3 = %EVR
Obsoletes: mbrola-voice-us3 < %EVR

%description us3
%summary

%files us3
%dir %_datadir/mbrola/us3
%_datadir/mbrola/us3/*

%package af1
Summary: af1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description af1
%summary

%files af1
%dir %_datadir/mbrola/af1
%_datadir/mbrola/af1/*

%package ar1
Summary: ar1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description ar1
%summary

%files ar1
%dir %_datadir/mbrola/ar1
%_datadir/mbrola/ar1/*

%package ar2
Summary: ar2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description ar2
%summary

%files ar2
%dir %_datadir/mbrola/ar2
%_datadir/mbrola/ar2/*

%package br1
Summary: br1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description br1
%summary

%files br1
%dir %_datadir/mbrola/br1
%_datadir/mbrola/br1/*

%package br2
Summary: br2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description br2
%summary

%files br2
%dir %_datadir/mbrola/br2
%_datadir/mbrola/br2/*

%package br3
Summary: br3 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description br3
%summary

%files br3
%dir %_datadir/mbrola/br3
%_datadir/mbrola/br3/*

%package br4
Summary: br4 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description br4
%summary

%files br4
%dir %_datadir/mbrola/br4
%_datadir/mbrola/br4/*

%package bz1
Summary: bz1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description bz1
%summary

%files bz1
%dir %_datadir/mbrola/bz1
%_datadir/mbrola/bz1/*

%package ca1
Summary: ca1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description ca1
%summary

%files ca1
%dir %_datadir/mbrola/ca1
%_datadir/mbrola/ca1/*

%package ca2
Summary: ca2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description ca2
%summary

%files ca2
%dir %_datadir/mbrola/ca2
%_datadir/mbrola/ca2/*

%package cn1
Summary: cn1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description cn1
%summary

%files cn1
%dir %_datadir/mbrola/cn1
%_datadir/mbrola/cn1/*

%package cr1
Summary: cr1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description cr1
%summary

%files cr1
%dir %_datadir/mbrola/cr1
%_datadir/mbrola/cr1/*

%package cz1
Summary: cz1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description cz1
%summary

%files cz1
%dir %_datadir/mbrola/cz1
%_datadir/mbrola/cz1/*

%package cz2
Summary: cz2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description cz2
%summary

%files cz2
%dir %_datadir/mbrola/cz2
%_datadir/mbrola/cz2/*

%package de1
Summary: de1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description de1
%summary

%files de1
%dir %_datadir/mbrola/de1
%_datadir/mbrola/de1/*

%package de2
Summary: de2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description de2
%summary

%files de2
%dir %_datadir/mbrola/de2
%_datadir/mbrola/de2/*

%package de3
Summary: de3 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description de3
%summary

%files de3
%dir %_datadir/mbrola/de3
%_datadir/mbrola/de3/*

%package de4
Summary: de4 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description de4
%summary

%files de4
%dir %_datadir/mbrola/de4
%_datadir/mbrola/de4/*

%package de5
Summary: de5 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description de5
%summary

%files de5
%dir %_datadir/mbrola/de5
%_datadir/mbrola/de5/*

%package de6
Summary: de6 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description de6
%summary

%files de6
%dir %_datadir/mbrola/de6
%_datadir/mbrola/de6/*

%package de7
Summary: de7 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description de7
%summary

%files de7
%dir %_datadir/mbrola/de7
%_datadir/mbrola/de7/*

%package de8
Summary: de8 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description de8
%summary

%files de8
%dir %_datadir/mbrola/de8
%_datadir/mbrola/de8/*

%package ee1
Summary: ee1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description ee1
%summary

%files ee1
%dir %_datadir/mbrola/ee1
%_datadir/mbrola/ee1/*

%package es1
Summary: es1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description es1
%summary

%files es1
%dir %_datadir/mbrola/es1
%_datadir/mbrola/es1/*

%package es2
Summary: es2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description es2
%summary

%files es2
%dir %_datadir/mbrola/es2
%_datadir/mbrola/es2/*

%package es3
Summary: es3 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description es3
%summary

%files es3
%dir %_datadir/mbrola/es3
%_datadir/mbrola/es3/*
%_datadir/mbrola/es3/._license.txt

%package es4
Summary: es4 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description es4
%summary

%files es4
%dir %_datadir/mbrola/es4
%_datadir/mbrola/es4/*

%package fr1
Summary: fr1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description fr1
%summary

%files fr1
%dir %_datadir/mbrola/fr1
%_datadir/mbrola/fr1/*

%package fr2
Summary: fr2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description fr2
%summary

%files fr2
%dir %_datadir/mbrola/fr2
%_datadir/mbrola/fr2/*

%package fr3
Summary: fr3 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description fr3
%summary

%files fr3
%dir %_datadir/mbrola/fr3
%_datadir/mbrola/fr3/*

%package fr4
Summary: fr4 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description fr4
%summary

%files fr4
%dir %_datadir/mbrola/fr4
%_datadir/mbrola/fr4/*

%package fr5
Summary: fr5 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description fr5
%summary

%files fr5
%dir %_datadir/mbrola/fr5
%_datadir/mbrola/fr5/*

%package fr6
Summary: fr6 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description fr6
%summary

%files fr6
%dir %_datadir/mbrola/fr6
%_datadir/mbrola/fr6/*

%package fr7
Summary: fr7 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description fr7
%summary

%files fr7
%dir %_datadir/mbrola/fr7
%_datadir/mbrola/fr7/*

%package gr1
Summary: gr1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description gr1
%summary

%files gr1
%dir %_datadir/mbrola/gr1
%_datadir/mbrola/gr1/*

%package gr2
Summary: gr2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description gr2
%summary

%files gr2
%dir %_datadir/mbrola/gr2
%_datadir/mbrola/gr2/*

%package hb1
Summary: hb1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description hb1
%summary

%files hb1
%dir %_datadir/mbrola/hb1
%_datadir/mbrola/hb1/*

%package hb2
Summary: hb2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description hb2
%summary

%files hb2
%dir %_datadir/mbrola/hb2
%_datadir/mbrola/hb2/*

%package hn1
Summary: hn1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description hn1
%summary

%files hn1
%dir %_datadir/mbrola/hn1
%_datadir/mbrola/hn1/*

%package hu1
Summary: hu1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description hu1
%summary

%files hu1
%dir %_datadir/mbrola/hu1
%_datadir/mbrola/hu1/*

%package ic1
Summary: ic1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description ic1
%summary

%files ic1
%dir %_datadir/mbrola/ic1
%_datadir/mbrola/ic1/*

%package id1
Summary: id1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description id1
%summary

%files id1
%dir %_datadir/mbrola/id1
%_datadir/mbrola/id1/*

%package in1
Summary: in1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description in1
%summary

%files in1
%dir %_datadir/mbrola/in1
%_datadir/mbrola/in1/*

%package in2
Summary: in2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description in2
%summary

%files in2
%dir %_datadir/mbrola/in2
%_datadir/mbrola/in2/*

%package ir1
Summary: ir1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description ir1
%summary

%files ir1
%dir %_datadir/mbrola/ir1
%_datadir/mbrola/ir1/*

%package it1
Summary: it1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description it1
%summary

%files it1
%dir %_datadir/mbrola/it1
%_datadir/mbrola/it1/*

%package it2
Summary: it2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description it2
%summary

%files it2
%dir %_datadir/mbrola/it2
%_datadir/mbrola/it2/*

%package it3
Summary: it3 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description it3
%summary

%files it3
%dir %_datadir/mbrola/it3
%_datadir/mbrola/it3/*

%package it4
Summary: it4 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description it4
%summary

%files it4
%dir %_datadir/mbrola/it4
%_datadir/mbrola/it4/*

%package jp1
Summary: jp1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description jp1
%summary

%files jp1
%dir %_datadir/mbrola/jp1
%_datadir/mbrola/jp1/*

%package jp2
Summary: jp2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description jp2
%summary

%files jp2
%dir %_datadir/mbrola/jp2
%_datadir/mbrola/jp2/*

%package jp3
Summary: jp3 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description jp3
%summary

%files jp3
%dir %_datadir/mbrola/jp3
%_datadir/mbrola/jp3/*

%package la1
Summary: la1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description la1
%summary

%files la1
%dir %_datadir/mbrola/la1
%_datadir/mbrola/la1/*

%package lt1
Summary: lt1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description lt1
%summary

%files lt1
%dir %_datadir/mbrola/lt1
%_datadir/mbrola/lt1/*

%package lt2
Summary: lt2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description lt2
%summary

%files lt2
%dir %_datadir/mbrola/lt2
%_datadir/mbrola/lt2/*

%package ma1
Summary: ma1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description ma1
%summary

%files ma1
%dir %_datadir/mbrola/ma1
%_datadir/mbrola/ma1/*

%package mx1
Summary: mx1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description mx1
%summary

%files mx1
%dir %_datadir/mbrola/mx1
%_datadir/mbrola/mx1/*

%package mx2
Summary: mx2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description mx2
%summary

%files mx2
%dir %_datadir/mbrola/mx2
%_datadir/mbrola/mx2/*

%package nl1
Summary: nl1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description nl1
%summary

%files nl1
%dir %_datadir/mbrola/nl1
%_datadir/mbrola/nl1/*

%package nl2
Summary: nl2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description nl2
%summary

%files nl2
%dir %_datadir/mbrola/nl2
%_datadir/mbrola/nl2/*

%package nl3
Summary: nl3 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description nl3
%summary

%files nl3
%dir %_datadir/mbrola/nl3
%_datadir/mbrola/nl3/*

%package nz1
Summary: nz1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description nz1
%summary

%files nz1
%dir %_datadir/mbrola/nz1
%_datadir/mbrola/nz1/*

%package pl1
Summary: pl1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description pl1
%summary

%files pl1
%dir %_datadir/mbrola/pl1
%_datadir/mbrola/pl1/*

%package pt1
Summary: pt1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description pt1
%summary

%files pt1
%dir %_datadir/mbrola/pt1
%_datadir/mbrola/pt1/*

%package ro1
Summary: ro1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description ro1
%summary

%files ro1
%dir %_datadir/mbrola/ro1
%_datadir/mbrola/ro1/*

%package sw1
Summary: sw1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description sw1
%summary

%files sw1
%dir %_datadir/mbrola/sw1
%_datadir/mbrola/sw1/*

%package sw2
Summary: sw2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description sw2
%summary

%files sw2
%dir %_datadir/mbrola/sw2
%_datadir/mbrola/sw2/*

%package tl1
Summary: tl1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description tl1
%summary

%files tl1
%dir %_datadir/mbrola/tl1
%_datadir/mbrola/tl1/*

%package tr1
Summary: tr1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description tr1
%summary

%files tr1
%dir %_datadir/mbrola/tr1
%_datadir/mbrola/tr1/*

%package tr2
Summary: tr2 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description tr2
%summary

%files tr2
%dir %_datadir/mbrola/tr2
%_datadir/mbrola/tr2/*

%package vz1
Summary: vz1 voice for MBROLA
Group: Sound
BuildArch: noarch
Requires: mbrola

%description vz1
%summary

%files vz1
%dir %_datadir/mbrola/vz1
%_datadir/mbrola/vz1/*

%prep
%setup

%install
mkdir -pv %buildroot%_datadir/mbrola
cp -rv data/* %buildroot%_datadir/mbrola/

%changelog
* Thu Aug 22 2024 Artem Semenov <savoptik@altlinux.org> 20200332-alt1
- Initial build for Sisyphus (ALT bug: 51044)
