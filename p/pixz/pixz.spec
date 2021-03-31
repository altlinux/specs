
%define _unpackaged_files_terminate_build 1

Name:     pixz
Version:  1.0.7
Release:  alt1

Summary:  Parallel, indexed xz compressor
License:  BSD-2-Clause
Group:    Other
Url:      https://github.com/vasi/pixz

Source:   %name-%version.tar
Patch:    %name-%version-%release.patch

BuildRequires: pkgconfig(liblzma) pkgconfig(libarchive)
BuildRequires: /usr/bin/a2x

%description
Pixz (pronounced *pixie*) is a parallel, indexing version of 'xz'.

The existing XZ Utils provide great compression in the '.xz' file
format, but they produce just one big block of compressed data.
Pixz instead produces a collection of smaller blocks which makes
random access to the original data possible. This is especially
useful for large tarballs.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%_bindir/*
%_man1dir/*
%doc *.md

%changelog
* Wed Mar 31 2021 Ivan A. Melnikov <iv@altlinux.org> 1.0.7-alt1
- Initial build for Sisyphus
