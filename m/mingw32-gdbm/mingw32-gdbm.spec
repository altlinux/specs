BuildRequires: rpm-build-mingw32
BuildRequires: gcc-c++
%define __strip %{_mingw32_strip}
%define __objdump %{_mingw32_objdump}

Name:           mingw32-gdbm
Version:        1.8.0
Release:        alt2_6
Summary:        MinGW port of GNU database routines

License:        GPLv2+
Group:          System/Libraries
URL:            http://www.gnu.org/software/gdbm/
Source0:        ftp://ftp.gnu.org/gnu/gdbm/gdbm-%{version}.tar.gz

Patch0:         gdbm-1.8.0-jbj.patch
Patch1:         gdbm-1.8.0-fhs.patch
Patch2:         gdbm-1.8.0-cflags.patch
Patch3:         gdbm-1.8.0-64offset.patch

Patch1000:      mingw32-gdbm-1.8.0-windows.patch
Patch1001:      mingw32-gdbm-1.8.0-libtool-install.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 49
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  libtool
BuildRequires:  automake
Source44: import.info


%description
Gdbm is a GNU database indexing library, including routines which use
extensible hashing.  Gdbm works in a similar way to standard UNIX dbm
routines.  Gdbm is useful for developers who write C applications and
need access to a simple and efficient database or who are building C
applications which will use such a database.

This is the MinGW Windows port of the libraries and development tools.


%prep
%setup -q -n gdbm-%{version}
%patch0 -p 1 -b .jbj
%patch1 -p 1 -b .fhs
%patch2 -p 1 -b .cflags
%patch3 -p1 -b .offset

%patch1000 -p1 -b .windows
%patch1001 -p1 -b .libtool-install


%build
# Update the version of libtool.
libtoolize --force --copy

aclocal

# We want to update config.sub and config.guess because the ones
# shipped with gdbm are ancient history.  However note that there is
# no Makefile.am -- we are only using automake for convenience here!
rm -f config.sub config.guess
automake --add-missing ||:

autoconf

%{_mingw32_configure}
# NB: %{?_smp_mflags} causes build to fail.
make libdir=%{_mingw32_libdir} all progs


%install
make prefix=$RPM_BUILD_ROOT%{_mingw32_prefix} install

# Install the binaries.  Arguable whether we really want these.
install conv2gdbm.exe tdbm.exe testdbm.exe testgdbm.exe testndbm.exe tndbm.exe \
  $RPM_BUILD_ROOT%{_mingw32_bindir}

# Native Fedora package seems to fluff this, but as far as I
# can tell they are trying to create <gdbm/gdbm.h> which
# links to <gdbm.h>.
pushd $RPM_BUILD_ROOT%{_mingw32_includedir}
mkdir gdbm
cd gdbm
ln -s ../gdbm.h
popd

# Remove the static library.
rm $RPM_BUILD_ROOT%{_mingw32_libdir}/libgdbm.a

# Remove man page and info file which duplicate what is in native package.
rm -r $RPM_BUILD_ROOT%{_mingw32_prefix}/man
rm -r $RPM_BUILD_ROOT%{_mingw32_prefix}/info


%files
%{_mingw32_bindir}/conv2gdbm.exe
%{_mingw32_bindir}/tdbm.exe
%{_mingw32_bindir}/testdbm.exe
%{_mingw32_bindir}/testgdbm.exe
%{_mingw32_bindir}/testndbm.exe
%{_mingw32_bindir}/tndbm.exe
%{_mingw32_bindir}/libgdbm-2.dll
%{_mingw32_libdir}/libgdbm.dll.a
%{_mingw32_libdir}/libgdbm.la
%{_mingw32_includedir}/gdbm.h
%{_mingw32_includedir}/gdbm


%changelog
* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_6
- bugfix release by fcimport

* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_6
- initial release by fcimport

