%define pypi_name pelican

%def_without bootstrap
%def_with standalone_feedgenerator

%define full_desc \
Pelican is a static site generator, written in Python_.\
\
* Write your weblog entries directly with your editor of choice (vim!)\
  in reStructuredText_ or Markdown_\
* Includes a simple CLI tool to ...

%define short_desc A tool to generate a static blog from reStructuredText or Markdown input files

# Tests are bit unstable due comparing html attributes via diff
%def_without tests

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

Name: python3-module-%{pypi_name}
Version: 4.6.0
Release: alt3
Summary: %{short_desc}
Group: Development/Python3

License: AGPLv3
Url: http://getpelican.com/
# https://github.com/getpelican/%{pypi_name}/archive/%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
Source: %{pypi_name}-%{version}.tar

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-module-blinker
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-pytz
BuildRequires: python3-module-unidecode
BuildRequires: python3-module-mock
%if_without bootstrap
BuildRequires: python3-module-%{pypi_name}
BuildRequires: python3-module-nose
%endif

Obsoletes: python-module-%{pypi_name}
Conflicts: python-module-%{pypi_name}

%description
%{full_desc}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%package -n %{pypi_name}
Summary: %{short_desc}
Group: Publishing

Requires: python3-module-%{pypi_name}
%if_with standalone_feedgenerator
Requires: python3-module-feedgenerator
%endif
Requires: python3-module-markdown
Requires: python3-module-unidecode
Requires: python3-module-beautifulsoup4

%description -n %{pypi_name}
%{full_desc}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%prep
%setup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove bagpath #!/usr/bin/env from files
sed -i '1d' %{pypi_name}/tools/%{pypi_name}_import.py
sed -i '1d' %{pypi_name}/tools/%{pypi_name}_quickstart.py
sed -i '1d' %{pypi_name}/tools/%{pypi_name}_themes.py
sed -i '1d' %{pypi_name}/tools/templates/pelicanconf.py.jinja2
sed -i '1d' %{pypi_name}/tools/templates/publishconf.py.jinja2

# Substitute feedgenerator with it's original django
%if_without standalone_feedgenerator
sed -i 's|feedgenerator|django.utils.feedgenerator|' %{pypi_name}/writers.py
sed -i "s|'feedgenerator >= 1.9', ||" setup.py
%endif

# Calm down the rpm-build-python3 utility
touch %{pypi_name}/plugins/__init__.py

%build
%{python3_build}

# Build docs (can't be exec without python3-module-%{pypi_name} itself!)
%if_without bootstrap
sphinx-build-3 docs html
# Remove leftovers from sphinxbuild
rm html/_static/theme-basic.zip
rm -rf html/_downloads/* html/.doctrees html/.buildinfo
%endif

%install
%{python3_install}

%check
%if_with tests
nosetests-3 -sv --with-coverage --cover-package=%{pypi_name} %{pypi_name}
%endif

%files
%if_without bootstrap
%doc html
%endif
%doc README.rst LICENSE
%_bindir/%{pypi_name}
%_bindir/%{pypi_name}-import
%_bindir/%{pypi_name}-quickstart
%_bindir/%{pypi_name}-themes
%{python3_sitelibdir_noarch}/%{pypi_name}
%{python3_sitelibdir_noarch}/%{pypi_name}-%{version}-py*.*.egg-info

%files -n %{pypi_name}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%changelog
* Mon Feb 07 2022 Alexey Appolonov <alexey@altlinux.org> 4.6.0-alt3
- Fixed build (the build was broken after python3 upgrade to v3.10).

* Tue Jul 06 2021 Alexey Appolonov <alexey@altlinux.org> 4.6.0-alt2
- Requirement of the "python3-module-beautifulsoup4" package, which some of
  the plugins can use.

* Tue Jun 29 2021 Alexey Appolonov <alexey@altlinux.org> 4.6.0-alt1
- New version.

* Fri Mar 27 2020 Alexey Appolonov <alexey@altlinux.org> 4.1.0-alt5
- Fixed build.

* Thu Sep 12 2019 Alexey Appolonov <alexey@altlinux.org> 4.1.0-alt4
- Proper build with python3 (with docs);
- Use of standalone feedgenerator.

* Tue Aug 22 2019 Alexey Appolonov <alexey@altlinux.org> 4.1.0-alt3
- First build with python3 (no docs).

* Tue Aug 06 2019 Alexey Appolonov <alexey@altlinux.org> 4.1.0-alt2
- Proper substitution of feedgenerator with it's original django.

* Mon Jul 15 2019 Andrey Cherepanov <cas@altlinux.org> 4.1.0-alt1
- New version.

* Tue Dec 04 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.1-alt1
- New version.

* Fri Nov 16 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- New version.

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt1
- new version 3.7.1

* Thu Jul 14 2016 Andrey Cherepanov <cas@altlinux.org> 3.6.3-alt2
- Add metapackage pelican with all requirements needed for generation

* Wed Jul 13 2016 Andrey Cherepanov <cas@altlinux.org> 3.6.3-alt1
- new version 3.6.3

* Wed Apr 01 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.5.0-alt1
- Initial build.
