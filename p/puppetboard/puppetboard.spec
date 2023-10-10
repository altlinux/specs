Name:    puppetboard
Version: 5.1.0
Release: alt1

Summary: Web frontend for PuppetDB
License: Apache-2.0
Group:   Development/Python
URL:     https://github.com/voxpupuli/puppetboard

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-apache2
BuildRequires: python3-dev python3-module-setuptools
# Requirement see at requirements.txt
BuildRequires: python3-module-flask >= 1.1.1
BuildRequires: python3-module-flask-wtf >= 0.14.2
BuildRequires: python3-module-jinja2 >= 2.10.3
BuildRequires: python3-module-markupsafe >= 1.1.1
BuildRequires: python3-module-wtforms >= 2.2.1
BuildRequires: python3-module-werkzeug >= 0.16.0
BuildRequires: python3-module-itsdangerous >= 1.1.0
BuildRequires: python3-module-pypuppetdb >= 2.1.0
BuildRequires: python3-module-requests >= 2.22.0
BuildRequires: python3-module-commonmark = 0.9.1

BuildArch: noarch

Source:  %name-%version.tar
Source1: wsgi.py
Source2: %name.conf
Source3: %name.start

Requires: python3-module-commonmark >= 0.9.1

%define wsgi_dir %_datadir/puppetboard

%description
Puppetboard is a web interface to PuppetDB aiming to replace the
reporting functionality of Puppet Dashboard. Puppetboard relies on the
pypuppetdb library to fetch data from PuppetDB and is built with the
help of the Flask microframework.

%package apache2
Summary: Apache + mod_wsgi support for puppetboard
Group:   Development/Python
Requires: %name = %EVR
Requires: apache2-base
Requires: apache2-mod_wsgi-py3

%description apache2
This package provides support for running puppetboard under Apache2 + mod_wsgi

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install
rm -rf %buildroot%python3_sitelibdir/test
install -Dm0644 %name/default_settings.py %buildroot/%wsgi_dir/settings.py
install -Dm0644 %SOURCE1 %buildroot/%wsgi_dir
install -Dm0644 %SOURCE2 %buildroot/%apache2_sites_available/%name.conf
mkdir -p %buildroot%apache2_sites_enabled
touch %buildroot%apache2_sites_enabled/%name.conf
install -Dm0644 %SOURCE3 %buildroot%apache2_sites_start/100-%name.conf

sed -i -e 's|@PYTHON_SITELIB@|%python3_sitelibdir|' -e 's|@WSGI_DIR@|%wsgi_dir|' \
    %buildroot/%apache2_sites_available/%name.conf

sed -i -e 's|@WSGI_DIR@|%wsgi_dir|' %buildroot/%wsgi_dir/wsgi.py

subst '1i #!%__python3' %buildroot/%wsgi_dir/*.py

# Remove unnecessary files
rm -rf %buildroot%_prefix/requirements*

%pre
getent group puppetboard > /dev/null || /usr/sbin/groupadd -r puppetboard
getent passwd puppetboard > /dev/null || \
%_sbindir/useradd -M -r -g puppetboard -c 'Puppetboard Daemon' \
     -d / -s /sbin/nologin puppetboard 2> /dev/null ||:

%post apache2
%_sbindir/a2enmod wsgi-py3

%files
%doc *.md
%config(noreplace) %wsgi_dir/settings.py
%config(noreplace) %wsgi_dir/wsgi.py
%config(noreplace) %apache2_sites_available/%name.conf
%apache2_sites_start/*.conf
%ghost %apache2_sites_enabled/*.conf
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info
%dir %wsgi_dir

%changelog
* Tue Oct 10 2023 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- New version.

* Fri Jul 28 2023 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version.

* Tue May 02 2023 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version.

* Fri Jun 04 2021 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version.

* Fri Jul 31 2020 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version.

* Wed Apr 08 2020 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt1
- New version.

* Sat Apr 04 2020 Andrey Cherepanov <cas@altlinux.org> 2.1.1-alt1
- New version.

* Tue Mar 24 2020 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- New version.

* Mon Jan 20 2020 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Tue Oct 08 2019 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.

* Wed Sep 04 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- New version.

* Tue May 14 2019 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus (based on SUSE spec file).
