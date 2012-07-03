Name: git-bzr
Version: 1.1_48_g61d6007
Release: alt1.1
Summary: A bidirectional git - bazaar gateway
Group: Development/Other
License: GPL2
Url: http://github.com/kfish/git-bzr
Packager: Ildar Mulyukov <ildar@altlinux.ru>

BuildArch: noarch
Source: %name.tar

Requires: python-module-bzr-fastimport bzr
Requires: python-module-fastimport

%description
This script allows you to add bazaar repositories as git branches in your git
repository. After that, you can fetch the Bazaar repo, make some changes, and
push it back into Bazaar.

%prep
%setup -n %name

%install
mkdir -p %buildroot%_bindir
install %name -m 0755 %buildroot%_bindir

%files
%doc AUTHORS README TODO
%_bindir/%name

%changelog
* Tue Nov 29 2011 Michael Shigorin <mike@altlinux.org> 1.1_48_g61d6007-alt1.1
- NMU: added missing Requires: python-module-fastimport

* Sun Jul 18 2010 Ildar Mulyukov <ildar@altlinux.ru> 1.1_48_g61d6007-alt1
- code origin changed (see URL:)

* Tue Apr 28 2009 Boris Savelev <boris@altlinux.org> 0.1-alt1
- add buildreq and req (fix #19772)

* Sun Mar 01 2009 Boris Savelev <boris@altlinux.org> 0.1-alt0.1
- initial build

