%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%set_verify_elf_method strict,rpath=relaxed

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%def_with check

Name: presage
Version: 0.9.1
Release: alt1

Summary: intelligent predictive text entry platform
License: GPL-3.0-or-later
Group: Text tools
Url: https://git.code.sf.net/p/presage/presage-debian

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: gcc-c++
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(tinyxml)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(ncurses)
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: help2man

%if_with check
BuildRequires: pkgconfig(cppunit)
%endif

%description
Presage is an intelligent predictive text entry platform.

This package contains the tools required to generate custom
statistical data used by the presage predictive text engine to
generate predictions.

This package also contains simple demonstration programs and simulator

%package -n libpresage-data
Group: Other
Summary: intelligent predictive text entry platform (data files)
BuildArch: noarch

%description -n libpresage-data
Presage is an intelligent predictive text entry platform.

This package contains the sample statistical data files and
abbreviation files needed by presage.

%package -n libpresage1v5
Group: System/Libraries
Requires: libpresage-data
Summary: intelligent predictive text entry platform (shared library)

%description -n libpresage1v5
Presage is an intelligent predictive text entry platform.

A predictive text entry system attempts to improve the ease and speed
of textual input by predicting words. Word prediction consists in
computing which word tokens or word completions are most likely to be
entered next. The system analyses the text already entered and
combines the information thus extracted with other information sources
to calculate the set of most probable tokens.

Presage exploits redundant information embedded in natural
languages to generate word predictions. The modular architecture
allows its language model to be extended and customized to utilize
statistical, syntactic, and semantic information sources.

This package contains the shared library.

%package -n libpresage-devel
Group: Development/C++
Summary: intelligent predictive text entry platform (development files)
Requires: libpresage1v5 = %{version}-%{release}

%description -n libpresage-devel
Presage is an intelligent predictive text entry platform.

This package contains development files.

This package contains the header files needed to compile applications
or shared objects that use libpresage.

%package -n libpresage-doc
Group: Documentation
Summary: intelligent predictive text entry platform (documentation)
BuildArch: noarch

%description -n libpresage-doc
Presage is an intelligent predictive text entry platform.
This package contains the documentation for libpresage.

Documentation is available in HTML and LaTeX format.

%prep
%setup
%patch -p1

%build
%configure \
           --prefix=/usr \
           --sysconfdir=/etc \
           --mandir=/usr/share/man \
           --localstatedir=/var \
           --enable-documentation
%make

%install
%makeinstall_std

# remove static library
rm -vf %buildroot%_libdir/libpresage.a

%check
make check

%files
%doc AUTHORS ChangeLog COPYING FAQ NEWS README THANKS TODO
%_bindir/presage_demo
%_bindir/presage_demo_text
%_bindir/presage_simulator
%_bindir/text2ngram
%_man1dir/presage_demo.1.*
%_man1dir/presage_demo_text.1.*
%_man1dir/presage_simulator.1.*
%_man1dir/text2ngram.1.*
%dir %_datadir/presage
%_datadir/presage/presage.svg
%_datadir/presage/presage.xpm

%files -n libpresage-data
%_sysconfdir/presage.xml
%_datadir/presage/abbreviations_en.txt
%_datadir/presage/abbreviations_it.txt
%_datadir/presage/database_en.db
%_datadir/presage/database_es.db
%_datadir/presage/database_it.db
%_datadir/presage/presage.png

%files -n libpresage1v5
%_libdir/libpresage.so.1
%_libdir/libpresage.so.1.1.1

%files -n libpresage-devel
%_includedir/presage.h
%_includedir/presageCallback.h
%_includedir/presageException.h
%_libdir/libpresage.so

%files -n libpresage-doc
%_datadir/presage/python_binding.txt
%_datadir/presage/getting_started.txt
%dir %_datadir/presage/html
%_datadir/presage/html/*

%changelog
* Tue Jul 22 2025 Nikolay Strelkov <snk@altlinux.org> 0.9.1-alt1
- Initial build for Sisyphus
