Name: rpminstall-tests
Version: 1.0
Release: alt1

Summary: Tests for rpm: how it interprets packages when installing

License: %gpl2plus
Group: Development/Tools
Url: http://git.altlinux.org/people/imz/packages/rpminstall-tests.git

BuildArch: noarch

Requires: make rpm-build

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

%description
Tests for rpm: how it interprets packages when installing.

Now, it tests how various forms of constraints (Requires, Conflicts, Obsoletes)
are interpreted when they are installed together with packages with
various forms of matching Provides.

More tests can appear.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/%name
install -m0644 Makefile HELPER *.mk -t %buildroot%_datadir/%name/
install -m0755 makeme.sh -t %buildroot%_datadir/%name/

%check
# To pass the usual parallelism flags etc:
%global _make_bin ./makeme.sh
%make_build
# Also test with "Epoch: 0" instead of no Epoch:
%make_build clean
%make_build minimal_epoch=0

%files
%_datadir/%name

%changelog
* Tue Feb  5 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1
- initial build for ALT Linux Sisyphus.


