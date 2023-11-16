%define _unpackaged_files_terminate_build 1
%define pypi_name pelican

%def_without docs
%def_with check

Name: python3-module-%pypi_name
Version: 4.9.1
Release: alt1
Summary: Static site generator that supports Markdown and reST syntax
License: AGPL-3.0
Group: Development/Python3
Url: http://getpelican.com/
Vcs: https://github.com/getpelican/pelican
BuildArch: noarch
Source: %pypi_name-%version.tar

Requires: python3-module-beautifulsoup4
Requires: python3-module-markdown
Requires: python3-module-unidecode
Requires: python3-module-blinker
Requires: python3-module-jinja2
Requires: python3-module-Pygments
Requires: python3-module-docutils
Requires: python3-module-feedgenerator
Requires: python3-module-pytz
Requires: python3-module-rich
Requires: python3-module-dateutil

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pdm-backend
%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinxext-opengraph
BuildRequires: python3-module-livereload
BuildRequires: python3-module-furo
%endif
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-rich
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-pytz
BuildRequires: python3-module-blinker
BuildRequires: python3-module-feedgenerator
BuildRequires: python3-module-docutils
BuildRequires: python3-module-unidecode
BuildRequires: python3-module-typogrify
BuildRequires: /usr/bin/git
BuildRequires: python3-module-beautifulsoup4
BuildRequires: python3-module-lxml
BuildRequires: python3-module-markdown
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-watchfiles
BuildRequires: python3-module-ordered-set
%endif

Obsoletes: python-module-%pypi_name
Conflicts: python-module-%pypi_name

%add_python3_req_skip pelican.plugins

%description
Pelican is a static site generator, written in Python.
- Compose content in Markdown or reStructuredText using your editor of choice
- Simple command-line tool (re)generates HTML, CSS, and JS from your source content
- Easy to interface with version control systems and web hooks
- Completely static output is simple to host anywhere

%package -n %pypi_name
Summary: %summary
Group: Publishing
Requires: %name = %EVR
Requires: python3-module-markdown
Requires: python3-module-unidecode
Requires: python3-module-beautifulsoup4

%description -n %pypi_name
Pelican is a static site generator, written in Python.
- Compose content in Markdown or reStructuredText using your editor of choice
- Simple command-line tool (re)generates HTML, CSS, and JS from your source content
- Easy to interface with version control systems and web hooks
- Completely static output is simple to host anywhere

%package tests
Summary: Tests for %name
Group: Development/Python3
Requires: %name = %EVR

%description tests
Pelican is a static site generator, written in Python.
- Compose content in Markdown or reStructuredText using your editor of choice
- Simple command-line tool (re)generates HTML, CSS, and JS from your source content
- Easy to interface with version control systems and web hooks
- Completely static output is simple to host anywhere

This package contains tests for %pypi_name.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%if_with docs
# Build docs (can't be exec without python3-module-pelican itself!)
export PYTHONPATH=$PWD
sphinx-build-3 docs html
# Remove leftovers from sphinxbuild
rm html/_static/theme-basic.zip
rm -rf html/_downloads/* html/.doctrees html/.buildinfo
%endif

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%if_with docs
%doc html
%endif
%doc README.rst LICENSE
%_bindir/%pypi_name
%_bindir/pelican-import
%_bindir/pelican-plugins
%_bindir/pelican-quickstart
%_bindir/pelican-themes
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%pypi_name/tests

%files tests
%python3_sitelibdir/%pypi_name/tests

%files -n %pypi_name

%changelog
* Thu Nov 16 2023 Anton Vyatkin <toni@altlinux.org> 4.9.1-alt1
- New version 4.9.1.

* Tue Nov 14 2023 Anton Vyatkin <toni@altlinux.org> 4.9.0-alt1
- New version 4.9.0 (closes: #36804).

* Tue Jul 25 2023 Anton Vyatkin <toni@altlinux.org> 4.8.0-alt1
- New version 4.8.0.

* Mon Apr 17 2023 Anton Vyatkin <toni@altlinux.org> 4.6.0-alt7
- Fix BuildRequires.

* Thu May 19 2022 Alexey Appolonov <alexey@altlinux.org> 4.6.0-alt6
- Proper build that includes documentation.

* Thu May 19 2022 Alexey Appolonov <alexey@altlinux.org> 4.6.0-alt5
- Fixed build indeed (another import directive is changed in the same way).

* Thu May 19 2022 Alexey Appolonov <alexey@altlinux.org> 4.6.0-alt4
- Fixed build (could not import class "Markup" from module "jinja2");
- No docs (pelican use itself to generate the docs and the current build is
  broken).

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
