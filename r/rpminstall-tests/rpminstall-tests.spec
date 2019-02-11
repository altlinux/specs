Name: rpminstall-tests
Version: 1.0
Release: alt3

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

%package checkinstall
Summary: Immediately run %name when installing this package
Group: Other
Requires(pre): %name

%description checkinstall
Immediately run %name when installing this package.

They test rpm (applied to the results of rpm-build).

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

%files checkinstall

%pre checkinstall
# --pidfile doesn't exist and makes it always start.
/sbin/start-stop-daemon --start --pidfile /var/empty/no.pid \
--chuid nobody:nobody \
--startas /bin/sh -- -ec \
'export TMPDIR=/tmp; \
. /usr/lib/rpm/tmpdir.sh; \
cd  "$tmpdir"; \
%_datadir/%name/makeme.sh; \
%_datadir/%name/makeme.sh clean; \
%_datadir/%name/makeme.sh minimal_epoch=0; \
'

%changelog
* Mon Feb 11 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt3
- Unmarked XFAIL: cases with underspecified Provides
  (the error should be gone with rpm-4,13-alt6).
- Marked XFAIL: non-critical unrealistic cases when obsoleting an exact disttag.
 (Of course, this requires a fix, but this is not critical.)

* Sun Feb 10 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt2
- Additionally test the same things, but provided as virtual Provides
  (dummy = ...).
- Implemented a checkinstall subpackage that runs these tests immediately.
- Fixed running the tests from another working dir.

* Tue Feb  5 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1
- initial build for ALT Linux Sisyphus.


