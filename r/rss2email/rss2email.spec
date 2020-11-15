Name: rss2email
Version: 3.12.2
Release: alt1

Summary: Receive RSS or Atom feeds by email
License: GPL-2.0-only or GPL-3.0-only
Group: Networking/News
Url: https://github.com/rss2email/rss2email
Vcs: git://git.altlinux.org/gears/r/rss2email.git
BuildArch: noarch
Source: %name-%version-%release.tar

Requires: python3-module-%name = %EVR

BuildRequires: rpm-build-python3
BuildRequires: python3-module-feedparser
BuildRequires: python3-module-html2text

%description
rss2email is a simple program which you can run in your crontab.
It watches RSS (or Atom) feeds and sends you a nicely formatted
email message for each new item.

%package -n python3-module-%name
Summary: %name python3 module
Group: Development/Python3
License: GPL-2.0-only or GPL-3.0-only
Conflicts: %name < %version

%description -n python3-module-%name
This package contains %name python3 module.

%prep
%setup -n %name-%version-%release

%build
%python3_build

%install
%python3_install
install -pm755 r2e-migrate %buildroot%_bindir/
mkdir -p %buildroot%_man1dir
install -pm644 r2e.1 r2e-migrate.1 %buildroot%_man1dir/

%check
PATH="$PATH:%buildroot%_bindir" PYTHONPATH=%buildroot%python3_sitelibdir \
	%__python3 ./test/test.py

%define _unpackaged_files_terminate_build 1

%files
%_bindir/r2e
%_bindir/r2e-migrate
%_man1dir/r2e.1*
%_man1dir/r2e-migrate.1*
%doc AUTHORS CHANGELOG README.rst README.migrate

%files -n python3-module-%name
%python3_sitelibdir/%{name}*

%changelog
* Sun Nov 15 2020 Dmitry V. Levin <ldv@altlinux.org> 3.12.2-alt1
- 3.12.1 -> 3.12.2.
- Moved python3 module into separate subpackage.

* Sun Aug 16 2020 Dmitry V. Levin <ldv@altlinux.org> 3.12.1-alt1
- 2.71 -> 3.12.1.
- Packaged r2e-migrate to help with migration from rss2email 2.x
  to rss2email 3.x which introduced a new, incompatible format
  for configuration and feed data.

* Sun Apr 07 2013 Dmitry V. Levin <ldv@altlinux.org> 2.71-alt1
- Updated to 2.71.
- Imported patches from Debian and Fedora.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.65-alt1.1
- Rebuild with Python-2.7

* Mon Feb 01 2010 Dmitry V. Levin <ldv@altlinux.org> 2.65-alt1
- Initial revision.
