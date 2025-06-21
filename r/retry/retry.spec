%define _unpackaged_files_terminate_build 1

Name: retry
Version: 1.0.6
Release: alt1

Summary: Retry a command until the command succeeds
License: Apache-2.0
Group: Other
Url: https://github.com/minfrin/retry

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: txt2man

%description
Retry captures stdin into memory as the data is passed to the repeated
command, and this captured stdin is then replayed should the command be
repeated. This makes it possible to embed the retry tool into shell
pipelines.

Retry captures stdout into memory, and if the command was successful
stdout is passed on to stdout as normal, while if the command was
repeated stdout is passed to stderr instead. This ensures that output is
passed to stdout once and once only.

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
%doc AUTHORS ChangeLog COPYING LICENSE NEWS README.md
%_bindir/%name
%_man1dir/%{name}.1.*

%changelog
* Sat Jun 21 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.6-alt1
- Initial build for Sisyphus
