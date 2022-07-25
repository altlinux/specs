%define _unpackaged_files_terminate_build 1

Name: python3-module-fontawesome-markdown
Version: 0.5.0
Release: alt1

Summary: Markdown extension to use Font Awesome icons in a GitHub style
License: GPL-3.0
Group: Development/Python3
Url: https://github.com/bmcorser/fontawesome-markdown
BuildArch: noarch

Source0: %name-%version.tar
Patch0: python3-module-fontawesome-markdown-0.5.0-alt-update-to-markdown-3.patch
Patch1: python3-module-fontawesome-markdown-0.5.0-alt-remove-unused-modules.patch
Patch2: python3-module-fontawesome-markdown-0.5.0-alt-use-local-fontawesome-icons.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(markdown)
BuildRequires: fonts-otf-fontawesome5

%description
Font Awesome and Markdown, together!

For when words aren't enough.

A Markdown extension that looks for things like :fa-coffee: and
replaces them with the Font Awesome icon markup.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# update icons after patch2 (use icons from fonts-otf-fontawesome5)
pushd scripts
	%__python3 update_icon_list.py
popd

%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%python3_sitelibdir/*

%changelog
* Mon Jul 25 2022 Anton Zhukharev <ancieg@altlinux.org> 0.5.0-alt1
- initial build for Sisyphus

