
%global modname alembic

Name: python-module-alembic
Version: 0.6.3
Release: alt1

Summary: Database migration tool for SQLAlchemy

License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/alembic

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/a/%modname/%modname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python

BuildRequires: help2man
BuildRequires: python-devel
BuildRequires: python-module-mako

BuildRequires: python-module-nose
BuildRequires: python-module-SQLAlchemy >= 0.7.4

%description
Alembic is a new database migrations tool, written by the author of
SQLAlchemy <http://www.sqlalchemy.org>.  A migrations tool offers the
following functionality:

* Can emit ALTER statements to a database in order to change the structure
of tables and other constructs.
* Provides a system whereby "migration scripts" may be constructed; each script
indicates a particular series of steps that can "upgrade" a target database to
a new version, and optionally a series of steps that can "downgrade"
similarly, doing the same steps in reverse.
* Allows the scripts to execute in some sequential manner.

Documentation and status of Alembic is at http://readthedocs.org/docs/alembic/

%prep
%setup -n %modname-%version

%build
%python_build

mkdir bin
echo 'python -c "import alembic.config; alembic.config.main()" $*' > bin/alembic
chmod 0755 bin/alembic
help2man --version-string %{version} --no-info -s 1 bin/alembic > alembic.1

%install
%python_install
mkdir -p %buildroot%_man1dir/
install -m 0644 alembic.1 %buildroot%_man1dir/alembic.1

%files
%doc README.rst LICENSE CHANGES docs
%python_sitelibdir_noarch/%modname/
%python_sitelibdir_noarch/%modname-%{version}*
%_bindir/%modname
%_man1dir/alembic.1*

%changelog
* Wed Apr 02 2014 Vitaly Lipatov <lav@altlinux.ru> 0.6.3-alt1
- new version 0.6.3 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- new version 0.5.0 (with rpmrb script)

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt2
- initial build for ALT Linux Sisyphus

* Thu Mar 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_1
- update to new release by fcimport

* Thu Mar 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt2_11
- update to new release by fcimport

* Tue Jan 29 2013 Cronbuild Service <cronbuild@altlinux.org> 0.3.4-alt2_4
- rebuild to get rid of unmets

* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt1_4
- initial fc import

