# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/col /usr/bin/dvipdf /usr/bin/dvips /usr/bin/emacs /usr/bin/emacsclient /usr/bin/gconftool-2 /usr/bin/gdb /usr/bin/groff /usr/bin/gvim /usr/bin/gzip /usr/bin/ldd /usr/bin/md5sum /usr/bin/perl /usr/bin/pkg-config /usr/bin/valgrind /usr/bin/xemacs bzlib-devel gcc-c++ gcc-fortran glib2-devel libX11-devel libao-devel libdbus-devel libfuse-devel libgcrypt-devel libgmp-devel libncurses-devel libreadline-devel pkgconfig(gconf-2.0) pkgconfig(gdk-pixbuf-xlib-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(libglade-2.0) pkgconfig(x11) python-devel unzip zlib-devel
# END SourceDeps(oneline)
Summary:  Fuzzing framework
Name: autodafe
Version: 0.1
Release: alt1_6
License: GPLv2+
Group: Development/Tools
URL: http://autodafe.sourceforge.net/
Source: http://downloads.sourceforge.net/autodafe/autodafe-%{version}.tar.gz
Patch1: autodafe.patch
Patch2: autodafe-0.1-cflags.patch

BuildRequires: libxml2-devel >= 2.6.13
BuildRequires: gdb >= 6.2
BuildRequires: gcc >= 3.3.4
BuildRequires: perl >= 3.3.4
BuildRequires: bison
BuildRequires: flex
Source44: import.info

%description
AutodafA. is a fuzzing framework able to uncover buffer overflows 
by using the fuzzing by weighting attacks with markers technique. 

%package doc
Summary:  Documentation of autodafe
Group:    Documentation
BuildArch:noarch

%description doc
This package contains tutorial to Autodafe

%prep
%setup -q
%patch1 -p1 -b .old
%patch2 -p1 -b .cflags
for i in README TUTORIAL; do iconv -f iso-8859-1 -t utf-8 < $i > $i.NEW && mv -f $i.NEW $i; done
cd docs; tar cfz tutorials.tgz tutorials

%build
%configure
make # do not use it in broken Makefile %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
make prefix=$RPM_BUILD_ROOT/usr -C src/adbg install
make prefix=$RPM_BUILD_ROOT/usr -C src/adc install
make prefix=$RPM_BUILD_ROOT/usr -C src/autodafe install
make prefix=$RPM_BUILD_ROOT/usr -C src/pdml2ad install
( cd ./etc/generator; ./generator.sh . )
mv ./etc/generator/autodafe $RPM_BUILD_ROOT%{_datadir}

%files
%doc README COPYING AUTHORS FAQ TODO TUTORIAL BUGS
%dir %{_usr}/share/autodafe
%{_usr}/share/autodafe/*
%{_bindir}/adbg
%{_bindir}/adc
%{_bindir}/autodafe
%{_bindir}/pdml2ad

%files doc
%doc docs/tutorials.tgz

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_6
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_5
- initial release by fcimport

