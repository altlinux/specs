Name: picat
Version: 3.7.0
Release: alt1

Summary: Picat logical programming language
License: MPL-2.0
Group: Development/Other
Url: http://picat-lang.org/

Packager: %packager
Source: %name-%version.tar
Patch0: %name-3.6.8-alt-cases-defaults.patch
Patch1: %name-3.6.8-alt-DEFAULT-PICATPATH.patch

BuildRequires: gcc-c++

%description
Picat is a simple, and yet powerful, logic-based
multi-paradigm programming language aimed for
general-purpose applications. Picat is a rule-based
language, in which predicates, functions, and actors are
defined with pattern-matching rules. Picat can be
considered as more expressive and scalable Prolog.

%description -l ru_RU.UTF-8
Picat представляет собой простой, но мощный,
универсальный мультипарадигменный язык,
базирующийся на логическом программировании.
Picat базируется на сопоставлениях с образцом,
определяя через них предикаты, функции и акторы.
Picat можно рассматривать как более экспрессивный
и лучше масштабируемый Prolog.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%define libdir %_libdir/%name

cd emu
%make -f Makefile.linux64 -j5 -e DEFAULT_PICATPATH=%libdir

%install
mkdir -p %buildroot%_bindir/
install -pm755 emu/picat %buildroot%_bindir/

mkdir -p %buildroot%libdir
mkdir -p %buildroot%libdir/preloaded

install -pm644 lib/*.pi %buildroot%libdir/preloaded
install -pm644 lib2/*.pi %buildroot%libdir/

%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir
mkdir -p %buildroot%docdir/tex

install -pm644 doc/*.pdf %buildroot%docdir/
install -pm644 doc/*.tex %buildroot%docdir/tex/

install -pm644 INSTALL %buildroot%docdir/
install -pm644 LICENSE %buildroot%docdir/
install -pm644 README %buildroot%docdir/

%files
%_bindir/picat
%dir %docdir
%docdir/*

%dir %libdir
%libdir/*.pi
%dir %libdir/preloaded
%libdir/preloaded/*.pi

%changelog
* Wed Aug 28 2024 Andrey Bergman <vkni@altlinux.org> 3.7.0-alt1
- Version update.

* Sat Aug 24 2024 Andrey Bergman <vkni@altlinux.org> 3.6.8-alt1
- Initial release for Sisyphus.


