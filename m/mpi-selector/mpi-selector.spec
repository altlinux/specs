Summary: A simple tool to provide site-wide and per-user defaults for which MPI implementation to use

Name: mpi-selector
Version: 1.0.3
Release: alt2
License: BSD
Group: System/Base

Source: %name-%version.tar
Source1: post_mpi_selector
Source2: preun_mpi_selector
Source3: mpi-selector-manpath.sh
Source4: mpi-selector-manpath.csh

BuildArch: noarch

Packager: Stanislav Ievlev <inger@altlinux.org>
Requires: rpm-macros-%{name} = %{version}-%{release}
BuildRequires: perl-podlators

%description
A simple tool that allows system administrators to set a site-wide
default for which MPI implementation is to be used, but also allow
users to set their own defaults MPI implementation, thereby overriding
the site-wide default.

The default can be changed easily via the mpi-selector command --
editing of shell startup files is not required.


%package -n rpm-macros-%{name}
Summary: Set of RPM macros for packaging %name-based applications
Group: Development/Other

%description -n rpm-macros-%{name}
Set of RPM macros for packaging %name-based applications for ALT Linux.
Install this package if you want to create RPM packages that use %name.

%prep

%setup -q -n %name-%version


%build

%configure --with-shell-startup-dir=%buildroot%_sysconfdir/profile.d
%make_build


%install
%makeinstall

install -d -m 755 %buildroot%_localstatedir/%name/data
install -Dpm 644 /dev/null %buildroot%_sysconfdir/sysconfig/%name

install -d %buildroot%_sysconfdir/rpm/macros.d
cat >%buildroot%_sysconfdir/rpm/macros.d/%name<<EOF
%%post_mpi_selector %_sbindir/post_mpi_selector
%%preun_mpi_selector %_sbindir/preun_mpi_selector
EOF

install -Dpm755 %SOURCE1 %buildroot%_sbindir/post_mpi_selector
install -Dpm755 %SOURCE2 %buildroot%_sbindir/preun_mpi_selector

# Environment initialization scripts for Bash and CShell
install -d -m 755 %buildroot%_sysconfdir/profile.d
install -p -m 755 %SOURCE3 %buildroot%_sysconfdir/profile.d
install -p -m 755 %SOURCE4 %buildroot%_sysconfdir/profile.d

%files
%_bindir/*
%_sbindir/*
%_man1dir/*
#%_sysconfdir/rpm/macros.d/*
%_sysconfdir/profile.d/*
%_localstatedir/%name
%ghost %config(noreplace) %_sysconfdir/sysconfig/%name
%exclude %_sysconfdir/rpm/macros.d/*

%files -n rpm-macros-%{name}
%_sysconfdir/rpm/macros.d/*


%changelog
* Wed Nov 17 2010 Andriy Stepanov <stanv@altlinux.ru> 1.0.3-alt2
- Don't harmfull $MANPATH

* Fri Aug 13 2010 Andriy Stepanov <stanv@altlinux.ru> 1.0.3-alt1
- Version 1.0.3

* Mon May 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Version 1.0.2

* Fri Nov 21 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt3
- move rpm macros to separate package (Igor Vlasenko)

* Mon Nov 10 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt2
- fix post_mpi_selector: always call register to update mpivars.sh to new versions

* Thu Sep 18 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt1
- OFED 1.3.1

* Tue Jan 29 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt1
- Initial build
