%define pypi_name mat2
%def_without check

Name:    python3-module-%pypi_name
Version: 0.14.0
Release: alt2

License: LGPL-3.0
Group:   Development/Python3
URL:	 https://pypi.org/project/mat2
VCS:	 https://github.com/jvoisin/mat2

Summary: Metadata and privacy
Summary(ru_RU.UTF-8): Метаданные и конфиденциальность

Requires: libwebp-pixbuf-loader

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pycairo ffmpeg
BuildRequires: python3(gi) gir(GdkPixbuf)
BuildRequires: gir(Poppler) gir(Rsvg) itstool
BuildRequires: python3-module-mutagen perl-Image-ExifTool
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
This is precisely the job of mat2: getting rid, as much as possible, of
metadata.

%description -l ru_RU.UTF-8
Основная задача mat2: избавиться, насколько это возможно, от метаданных.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%_bindir/%pypi_name
%_datadir/man/man1/%pypi_name.1.xz
%python3_sitelibdir/lib%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc *.md LICENSE

%changelog
* Mon Jun 29 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.14.0-alt2
- added libwebp-pixbuf-loader depencety (ALT #59668)

* Wed Nov 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.14.0-alt1
- 0.13.5 -> 0.14.0
- change: VCS

* Sun Jan 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.13.5-alt3
- fix %%description -l ru_RU.UTF-8

* Thu Jan 09 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.13.5-alt2
- upstream update to git.6c966f2a

* Sat Nov 23 2024 Aleksandr Shamaraev <shad@altlinux.org> 0.13.5-alt1.d61fb7f7
- Initial build for Sisyphus.
