Name: virt-top
Version: 1.0.8
Release: alt1
Summary: Utility like top(1) for displaying virtualization stats
Group: Monitoring

License: GPLv2+
Url: http://people.redhat.com/~rjones/virt-top/
Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: %name-%version.tar

# Post-process output of CSV file (RHBZ#665817, RHBZ#912020).
Source1: processcsv.py
Source2: processcsv.py.pod

Patch: virt-top-1.0.4-processcsv-documentation.patch

# Update configure for aarch64 (bz #926701)
Patch1: virt-top-aarch64.patch

# Don't warn about immutable strings (OCaml 4.02).
Patch2: virt-top-no-immutable-warning.patch

# Kill -warn-error with fire.
Patch3: virt-top-1.0.8-no-warn-error.patch

BuildRequires: ocaml
BuildRequires: ocamldoc
BuildRequires: findlib
# Need the ncurses / ncursesw (--enable-widec) fix.
BuildRequires: ocaml-curses-devel >= 1.0.3
BuildRequires: ocaml-extlib
BuildRequires: ocaml-xml-light-devel
BuildRequires: ocaml-csv-devel
BuildRequires: ocaml-calendar-devel
# Need support for virDomainGetCPUStats (fixed in 0.6.1.2).
BuildRequires: ocaml-libvirt-devel >= 0.6.1.2

# Tortuous list of BRs for gettext.
BuildRequires: ocaml-gettext-devel >= 0.3.3
BuildRequires: ocaml-fileutils-devel

BuildRequires: libncurses-devel

# For msgfmt:
BuildRequires: gettext

# Non-OCaml BRs.
BuildRequires: libvirt-devel
BuildRequires: perl-Pod-Perldoc

%description
virt-top is a 'top(1)'-like utility for showing stats of virtualized
domains.  Many keys and command line options are the same as for
ordinary 'top'.

It uses libvirt so it is capable of showing stats across a variety of
different virtualization systems.

%prep
%setup

%patch0 -p1

# Update configure for aarch64 (bz #926701)
%patch1 -p1
%patch2 -p1
%patch3 -p1

chmod -x COPYING

%build
%configure
make all
make opt
strip virt-top/virt-top.opt

# Build translations.
make -C po

# Force rebuild of man page.
rm -f virt-top/virt-top.1
make -C virt-top virt-top.1

# Build processcsv.py.1.
pod2man -c "Virtualization Support" --release "%name-%version" \
%SOURCE2 > processcsv.py.1

%install
%makeinstall_std

# Install translations.
mkdir -p %buildroot%_datadir/locale
make -C po install PODIR="%buildroot%_datadir/locale"
%find_lang %name

# Install virt-top manpage by hand for now.
mkdir -p %buildroot%_man1dir
install -m 0644 virt-top/virt-top.1 %buildroot%_man1dir

# Install processcsv.py.
install -m 0755 %SOURCE1 %buildroot%_bindir

# Install processcsv.py(1).
install -m 0644 processcsv.py.1 %buildroot%_man1dir/

%files -f %name.lang
%doc COPYING README TODO ChangeLog
%_bindir/virt-top
%_man1dir/virt-top.1*
%_bindir/processcsv.py
%_man1dir/processcsv.py.1*

%changelog
* Tue Nov 22 2016 Lenar Shakirov <snejok@altlinux.ru> 1.0.8-alt1
- Initial build for ALT (based on 1.0.8-20.fc26.src)
