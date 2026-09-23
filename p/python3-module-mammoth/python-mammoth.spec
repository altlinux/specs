%define _unpackaged_files_terminate_build 1
%define pypi_name mammoth

Name: python3-module-%pypi_name
Version: 1.12.2
Release: alt1

Summary: Convert Word documents (.docx files) to HTML
License: BSD-2-Clause
Group: Development/Python3

Url: https://pypi.org/project/mammoth
Vcs: https://github.com/mwilliamson/python-mammoth

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

Source: %name-%version.tar

Patch: setup-alt-fixes.patch

%description
Mammoth is designed to convert .docx documents, such as
those created by Microsoft Word, Google Docs and LibreOffice,
and convert them to HTML. Mammoth aims to produce simple and
clean HTML by using semantic information in the document, and
ignoring other details. For instance, Mammoth converts any
paragraph with the style Heading 1 to h1 elements, rather than
attempting to exactly copy the styling (font, text size, colour,
etc.) of the heading.

There is a large mismatch between the structure used by .docx
and the structure of HTML, meaning that the conversion is unlikely
to be perfect for more complicated documents. Mammoth works best
if you only use styles to semantically mark up your document.

%prep
%setup
%patch -p0

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE *.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Sep 23 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.12.2-alt1
- Initial build for ALT Linux.

