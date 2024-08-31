%define _unpackaged_files_terminate_build 1
%define pypi_name mkdocs

%def_with check

Name: python3-module-%pypi_name
Version: 1.6.1
Release: alt1

Summary: Project documentation with Markdown
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/mkdocs/
Vcs: https://github.com/mkdocs/mkdocs
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif
BuildRequires: fonts-font-awesome

%description
MkDocs is a fast, simple and downright gorgeous static site generator
that's geared towards building project documentation. Documentation
source files are written in Markdown, and configured with a single YAML
configuration file.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

# unbundle font-awesome fonts
FONT_AWESOME_FONTS='%_datadir/fonts-font-awesome/fonts'

fonts_bundled=
for f in $(find -P %buildroot%python3_sitelibdir/mkdocs/themes/*/*/fonts/ -name 'fontawesome-webfont.*' -type f);
do
    printf "Found fontawesome font: '%%s'\n" "$f"
    font_name="$(basename "$f")"
    system_font="$FONT_AWESOME_FONTS/$font_name"
    if [ ! -f "$system_font" ]; then
        # raise to be sure we have synced fonts (bundled vs system)
        printf "Unknown font name: '%%s'\n" "$font_name"
        exit 1
    fi

    ln -sfT "$system_font" "$f"
    fonts_bundled=yes
done
[ "$fonts_bundled" != "yes" ] && exit 1

%check
# synced to pyproject.toml:tool.hatch.envs.test.scripts
%pyproject_run_unittest discover -p '*tests.py' mkdocs --top-level-directory .

%files
%_bindir/mkdocs
%python3_sitelibdir/mkdocs/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Aug 31 2024 Anton Vyatkin <toni@altlinux.org> 1.6.1-alt1
- New version 1.6.1.

* Mon Apr 22 2024 Anton Vyatkin <toni@altlinux.org> 1.6.0-alt1
- New version 1.6.0.

* Mon Feb 05 2024 Anton Vyatkin <toni@altlinux.org> 1.5.3-alt1
- New version 1.5.3.

* Thu Aug 03 2023 Stanislav Levin <slev@altlinux.org> 1.5.2-alt1
- 1.5.1 -> 1.5.2.

* Fri Jul 28 2023 Stanislav Levin <slev@altlinux.org> 1.5.1-alt1
- 1.5.0 -> 1.5.1.

* Thu Jul 27 2023 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1
- 1.4.3 -> 1.5.0.

* Wed May 03 2023 Stanislav Levin <slev@altlinux.org> 1.4.3-alt1
- 1.4.1 -> 1.4.3.

* Fri Oct 21 2022 Stanislav Levin <slev@altlinux.org> 1.4.1-alt2
- Fixed build without check.

* Mon Oct 17 2022 Stanislav Levin <slev@altlinux.org> 1.4.1-alt1
- 1.4.0 -> 1.4.1.

* Fri Oct 07 2022 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.3.1 -> 1.4.0.

* Fri Sep 23 2022 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- 1.3.0 -> 1.3.1.

* Thu May 19 2022 Fr. Br. George <george@altlinux.org> 1.3.0-alt1
- 1.2.3 -> 1.3.0
- Hack in external coverage call in tests

* Mon Jan 24 2022 Stanislav Levin <slev@altlinux.org> 1.2.3-alt1
- 1.2.2 -> 1.2.3 (closes: #41685).

* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt2
- fix build requires

* Mon Jul 19 2021 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1
- 1.0.4 -> 1.2.2.
- Enabled testing.

* Thu Jun 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.4-alt4
- drop excessive python3-module-jinja2-tests BR

* Mon Jun 01 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.4-alt3
- Requires fixed.

* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.4-alt2
- Build for python2 disabled.

* Wed Apr 24 2019 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.16.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Lenar Shakirov <snejok@altlinux.ru> 0.16.1-alt1
- 0.16.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.11.1-alt1.1
- NMU: Use buildreq for BR.

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1
- Initial build for Sisyphus

