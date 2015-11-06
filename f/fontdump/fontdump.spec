Group: Publishing
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
Name:           fontdump
Version:        1.3.0
Release:        alt1_2
Summary:        Dump the CSS and different formats of fonts for Google Fonts

License:        MIT
URL:            https://github.com/glasslion/fontdump
Source0:        https://pypi.python.org/packages/source/f/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
Requires:       python-module-setuptools
Source44: import.info

%description
A command line tool to dump the CSS and different formats of fonts for Google
Fonts, so you can serve them on your local servers.

%prep
%setup -q -n %{name}-%{version}
rm -rf *.egg-info

sed -i -e '/^#!\//, 1d' fontdump/cli.py fontdump/core.py

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root=%{buildroot}

%files
%doc PKG-INFO LICENSE
%{_bindir}/%{name}
%{python_sitelibdir_noarch}/%{name}/
%{python_sitelibdir_noarch}/%{name}-%{version}-py2.*.egg-info

%changelog
* Fri Nov 06 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_2
- new version

