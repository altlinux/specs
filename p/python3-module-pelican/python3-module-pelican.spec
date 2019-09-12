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
Version: 4.1.0
Release: alt4
Summary: %{short_desc}
Group: Development/Python3

License: AGPLv3
Url: http://getpelican.com/
# https://github.com/getpelican/pelican/archive/%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
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

%package -n pelican
Summary: %{short_desc}
Group: Publishing

Requires: python3-module-%{pypi_name}
%if_with standalone_feedgenerator
Requires: python3-module-feedgenerator
%endif
Requires: python3-module-markdown
Requires: python3-module-unidecode

%description -n pelican
%{full_desc}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%prep
%setup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# remove bagpath #!/usr/bin/env from files
sed -i '1d' pelican/tools/pelican_import.py
sed -i '1d' pelican/tools/pelican_quickstart.py
sed -i '1d' pelican/tools/pelican_themes.py
sed -i '1d' pelican/tools/templates/pelicanconf.py.jinja2
sed -i '1d' pelican/tools/templates/publishconf.py.jinja2

# substitute feedgenerator with it's original django
%if_without standalone_feedgenerator
sed -i 's|feedgenerator|django.utils.feedgenerator|' pelican/writers.py
sed -i "s|'feedgenerator >= 1.9', ||" setup.py
%endif

%build
%{python3_build}

# build docs (can't be exec without python3-module-pelican itself!)
%if_without bootstrap
sphinx-build-3 docs html
# remove leftovers from sphinxbuild
rm html/_downloads/theme-basic.zip html/_static/theme-basic.zip
rm -rf html/.doctrees html/.buildinfo
%endif

%install
%{python3_install}

%check
%if_with tests
nosetests-3 -sv --with-coverage --cover-package=pelican pelican
%endif

%files
%if_without bootstrap
%doc html
%endif
%doc README.rst LICENSE
%_bindir/pelican
%_bindir/pelican-import
%_bindir/pelican-quickstart
%_bindir/pelican-themes
%{python3_sitelibdir_noarch}/%{pypi_name}
%{python3_sitelibdir_noarch}/%{pypi_name}-*-py?.?.egg-info

%files -n pelican

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%changelog
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
