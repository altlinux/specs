%define _unpackaged_files_terminate_build 1

Name: python3-module-mdx_include
Version: 1.4.1
Release: alt1.gitd96b9b3

Summary: Python Markdown extension to include local or remote files
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/neurobin/mdx_include
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Include extension for Python Markdown. It lets you include local or
remote (downloadable) files into your markdown at arbitrary positions.

This project is motivated by markdown-include and provides the same
functionalities with some extras.

Inclusion for local file is by default recursive and for remote file
non-recursive. You can change this behavior through configuration.

You can include part of the file by slicing according to line/column number.

File/Downloaded contents are cached, i.e if you include same file multiple
times in multiple places, they won't be read/downloaded more than once.
This behavior can also be changed with configuration.

Circular inclusion by default raises an exception. You can change this behavior
to include the affected files in non-recursive mode through configuration.

You should not use markdown-include along with this extension, choose either
one, not both.

%prep
%setup

%build
%pyproject_build

cp LICENSE README.md %_builddir/

%install
%pyproject_install

%files
%doc LICENSE README.md
%python3_sitelibdir/*

%changelog
* Mon Jul 25 2022 Anton Zhukharev <ancieg@altlinux.org> 1.4.1-alt1.gitd96b9b3
- initial build for Sisyphus

