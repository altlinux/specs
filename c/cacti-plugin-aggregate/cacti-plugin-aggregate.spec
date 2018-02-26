%define _name aggregate
Name: cacti-plugin-%_name
Version: 0.75
Release: alt1

%define cactiplugindir %_datadir/cacti/plugins

Summary: This plugin aggregates graphs from Graph Management.

License: GPLv2+
Group: Monitoring

URL: http://docs.cacti.net/plugin:aggregate
Source0: %_name-v%version.tgz

Requires: cacti
BuildArch: noarch

%description
This plugin aggregates graphs from Graph Management.
All data you want to see must already be present on any existing graphs.

Features
 1) Aggregates existing Graphs into a single Aggregate Graph, keeping the sequence
 of selected Graphs and of the Graph Items within theses Graphs.
 2) Provides a new Graph Title for the Aggregate.
 3) Prepends all legend items with an optional text.
 4) Provides an algorithm to add additional <HR> linebreaks.
    This prevents ugly formatting.
 5) Allows for converting into AREA/STACK or LINE1 graphs
 6) Displays a list of Graph Items (taken from the first Graph selected) to allow
    for skipping selected graph items
 7) Allows for Totaling, either SIMILAR or ALL data sources
 8) Defines "Color Templates". These define a list of colors, e.g. light red to dark
    red. Allows to associate colored Graph Items to a Color Template. By doing so,
    Graph Items of same data source will no longer show the same color but instead
    will be colorized according to the Color Template

%prep
%setup -q -n %_name

%build

%install -n %name-%version
mkdir -p %buildroot%cactiplugindir/%_name

cp -a * %buildroot%cactiplugindir/%_name/
rm -rf %buildroot%cactiplugindir/%_name/{LICENSE,README,aggregate_manual.pdf}

%files
%doc LICENSE README aggregate_manual.pdf
%cactiplugindir/*

%changelog
* Mon Sep 27 2010 Alexey Shabalin <shaba@altlinux.ru> 0.75-alt1
- 0.7.5:
  + Bug Fix: better index checking for color items
  + Bug Fix: html validation errors fixed
  + Bug Fix: xss vulnerabilities fixed
  + Compat:  use buttons on action confirmation
  + Compat:  compatibility with PIA 2.8
  + Feature: Allow colors to rotate
  + Feature: "Total only" implemented
  + Feature: convert to all available LINEx graph item types
  + Feature: custom prefix on total GPRINTs
  + Feature: much more sophisticated graph item type conversion
  + Feature: support for |query_*| substitution on data query graphs.

* Wed May 19 2010 Alexey Shabalin <shaba@altlinux.ru> 0.74-alt1
- initial build
