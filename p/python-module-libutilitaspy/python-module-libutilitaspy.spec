Name: python-module-libutilitaspy
Version: 0.1
Release: alt1

%setup_python_module libutilitaspy

Summary: A general purpose library of data-structures, aspects, patterns and utilities for Python.
Source: %modulename-%{version}dev.tar.gz
License: Apache License 2.0
Group: Development/Python
Url: https://sites.google.com/site/libutilitaspy/home
Buildarch: noarch

# Automatically added by buildreq on Mon Jan 23 2012
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-email
BuildRequires: python-module-distribute

%description
                Features:
                * Data-structures:
                    - Stacks
                    - Heaps and priority queues
                    - Graphs
                    - Maps (generalizing both functions and dictionaries)
                    - Tries
                    - Partially Ordered Sets (Posets)
                    - (Reduced Ordered) Binary Decision Diagrams (BDDs)
                * Categories:
                    - Framework for defining entities from category theory: 
                        . categories, 
                        . objects, 
                        . arrows,
                        . diagrams (including empty, pairs, parallel arrows, spans and cospans)
                        . cones and cocones
                        . limits (general, final objects, products, equalizers, pullbacks)
                        . colimits (general, initial objects, coproducts, coequalizers, pushouts)
                    - Specific categories:
                        . Category of sets and functions
                *Patterns:
                    - Observer
                * Aspects:
                    - Framework for creating aspect classes (by subclassing or from a generator function)
                    - An aspect weaver meta-class factory
                    - Common aspects: method logger and method memoizer
                * General utilities:
                    - Generic pretty-printer for printable objects
                    - Name (identifier) generators
                    - Indenting/dedenting text
                    - Unzipping lists of pairs
                    - Common-prefix, postfix difference algorithms
                    - Infinity arithmetic
                etc.

%package docs
Group: Development/Python
Summary: Documentation and example files for %name

%description docs
Documentation and example files for %name

%prep
%setup -n %modulename-%{version}dev

%build
%python_build

%install
export PYTHONPATH=build/lib
%python_install

%files
%doc *txt
%python_sitelibdir_noarch/%{modulename}*
%dir %_datadir/%modulename
%_datadir/%modulename/config

%files docs
%_datadir/%modulename/[^c]*

%changelog
* Mon Jan 23 2012 Fr. Br. George <george@altlinux.ru> 0.1-alt1
- Initial build

