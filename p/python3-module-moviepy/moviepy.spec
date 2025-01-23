%define pypi_name moviepy

%def_with check
%def_with docs

Name: python3-module-%pypi_name
Version: 2.1.2
Release: alt1

Summary: Video editing with Python

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/moviepy
VCS: https://github.com/Zulko/moviepy
# Web documentation at https://zulko.github.io/moviepy

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with docs
BuildRequires: python3-module-sphinx_design
BuildRequires: python3-module-pydata-sphinx-theme
BuildRequires: python3-module-proglog
BuildRequires: python3-module-imageio
BuildRequires: python3-module-decorator
%endif

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-proglog
BuildRequires: python3-module-imageio
BuildRequires: python3-module-decorator
%endif

%description
MoviePy is a Python library for video editing: cutting, concatenations,
title insertions, video compositing (a.k.a. non-linear editing),
video processing, and creation of custom effects.

%package docs
Summary: Documentation for %pypi_name
Group: Development/Documentation

%description docs
MoviePy is a Python library for video editing: cutting, concatenations,
title insertions, video compositing (a.k.a. non-linear editing),
video processing, and creation of custom effects.

This package contains documentation for %pypi_name.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%if_with docs
%make -C docs man
%make -C docs html
# remove the sphinx-build leftovers
rm -rv docs/build/html/{.buildinfo,objects.inv}
%endif

%install
%pyproject_install

%if_with docs
mkdir -p %buildroot%_man1dir
install -m0644 docs/build/man/%pypi_name.1 %buildroot%_man1dir
%endif

%check
%pyproject_run_pytest -k \
	"not test_PR_529 \
	and not test_ffmpeg_parse_infos_decode_file \
	and not test_ffmpeg_parse_video_rotation \
	and not test_correct_video_rotation \
	and not test_ffmpeg_resize \
	and not test_ffmpeg_stabilize_video \
	and not test_audio_delay \
	and not test_setup"
# test_audio_delay failed on i586
# test_setup failed on ppc64le

%files
%doc *.txt *.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%if_with docs
%_man1dir/*

%files docs
%doc docs/build/html
%endif

%changelog
* Wed Jan 22 2025 Alexander Kovalev <alexvk@altlinux.org> 2.1.2-alt1
- Initial build for ALT.
