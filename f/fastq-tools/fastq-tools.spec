# SPDX-License-Identifier: MIT
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: fastq-tools
Version: 0.8.3
Release: alt1
Summary: Small utilities for working with fastq sequence files
License: MIT
Group: Sciences/Biology
Url: https://github.com/dcjones/fastq-tools

Source: %name-%version.tar
BuildRequires: libpcre-devel
BuildRequires: zlib-devel

%description
This package provides a number of small and efficient programs to
perform common tasks with high throughput sequencing data in the FASTQ
format. All of the programs work with typical FASTQ files as well as
gzipped FASTQ files.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
PATH=%buildroot%_bindir:$PATH
fastq-grep --version | grep -Fw 'fastq-grep (%name) %version'
%make_build check
echo -ne '@a:a\nAAA\n+\n000\n@b:b\nBBB\n+\n111\n@c:c\nCCC\n+\n222\n' > abc
fastq-grep BBB abc > b
fastq-grep -v BBB abc > ac
fastq-sort b ac > abc
sha256sum --check <<EOF
fe1ac8a7218d871a178b4447b4676b6a8e7149b371f1e166eb2d63ca6ecadc70  abc
03294ac689f1c5343f50fa969eb100014b77f051dbaa338cc484ac9f86079bf7  b
167b57abf6106792c70d348dd5dd3397f7b0222726ab3772e083885dbccf4f62  ac
EOF

%files
%define _customdocdir %_docdir/%name
%doc AUTHORS COPYING README.md
%_bindir/fastq-*
%_man1dir/fastq-*.1*

%changelog
* Wed Jun 05 2024 Vitaly Chikunov <vt@altlinux.org> 0.8.3-alt1
- First import v0.8.3 (2020-10-30).
