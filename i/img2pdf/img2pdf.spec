%define _unpackaged_files_terminate_build 1

%def_with check

Name: img2pdf
Version: 0.5.1
Release: alt1

Summary: Losslessly convert raster images to PDF
Group: Publishing
License: LGPLv3
URL: https://gitlab.mister-muffin.de/josch/img2pdf
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%set_pyproject_deps_check_filter pdfrw
%pyproject_builddeps_check
BuildRequires: python3-module-numpy-testing
BuildRequires: ImageMagick
%endif

%description
Python 3 library and command line utility img2pdf for losslessly converting
a bunch of image files into a PDF file. That means that the images
are either inserted into the PDF as-is or they are recompressed using
lossless compression. Thus, img2pdf usually runs faster and may yield
smaller PDF files than an ImageMagick convert command. The img2pdf command
complements the pdfimages command.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vk '(test_general or test_layout) and not animation.gif'

%files 
%doc README.md
%_bindir/%name
%exclude %_bindir/%name-gui
%python3_sitelibdir/*

%changelog
* Sat Mar 16 2024 Anton Kurachenko <srebrov@altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus.
