# Created by pyp2rpm-1.0.1
%global pypi_name python-subunit

Name:           python-module-subunit
Version:        0.0.18
Release:        alt1
Summary:        Python implementation of subunit test streaming protocol
Group:          Development/Python

License:        ASL 2.0
URL:            http://launchpad.net/subunit
Source0:        %{name}-%{version}.tar
Patch0:         unbundle-iso8601.patch
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-testtools
BuildRequires:  python-module-iso8601
BuildRequires:  python-module-extras

Requires:       python-module-testtools
Requires:       python-module-iso8601
Requires:       python-module-extras

%description
A streaming protocol for test results


%prep
%setup

%patch0 -p1

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove interpreter for non exec scripts
find python/subunit -name \*.py \! -perm /111 -exec \
  sed -i '1{/\/usr\/bin\/.*python/d}' {} +

%build
%python_build

%install
%python_install
# Reinstate +x for this script to avoid lint warning
chmod a+x %{buildroot}%{python_sitelibdir}/subunit/run.py

%check
# python 2.6 doesn't support test discovery
##TODO: Look into the issue with this test (attribute error with self.option)
#rm -f python/subunit/tests/test_output_filter.py
#
#PYTHONPATH=%{buildroot}%{python_sitelibdir} \
#%{__python} -m testtools.run discover python/subunit/tests

# Don't distribute the tests
rm -fr %{buildroot}%{python_sitelibdir}/subunit/tests

%files
%doc README NEWS
%{_bindir}/subunit2gtk
%{_bindir}/subunit2junitxml
%{_bindir}/subunit2pyunit
%{_bindir}/subunit-filter
%{_bindir}/subunit-ls
%{_bindir}/subunit-notify
%{_bindir}/subunit-output
%{_bindir}/subunit-stats
%{_bindir}/subunit-tags
%{_bindir}/tap2subunit
%{_bindir}/subunit-1to2
%{_bindir}/subunit-2to1
%{python_sitelibdir}/subunit
%{python_sitelibdir}/python_subunit-%{version}-py?.?.egg-info

%changelog
* Sat Aug 16 2014 Lenar Shakirov <snejok@altlinux.ru> 0.0.18-alt1
- First build for ALT (based on 0.0.18-1.el6.src)

