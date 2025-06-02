%define _unpackaged_files_terminate_build 1

Name: redir
Version: 3.3
Release: alt1

Summary: Redirect TCP connections
License: GPL-2.0
Group: Networking/Other
Url: https://github.com/troglobit/redir

Source: %name-%version.tar

#BuildRequires:

%description
redir is a TCP port redirector for UNIX. It can be run under inetd or as
a standalone daemon (in which case it handles multiple connections).
It is 8-bit clean, not limited to line mode, yet small and lightweight.
If you want access control, run it under xinetd or inetd with TCP
wrappers.

redir listens for TCP connections on a given SRC:PORT. When clients
connect to redir it initiates a connection to the server on DST:PORT
to pass data between them. The SRC and DST are from the perspective of
redir.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%doc AUTHORS ChangeLog.md COPYING README.md TODO transproxy.txt
%_bindir/*
%_man1dir/*
%exclude %_datadir/doc/%name/README.md
%exclude %_datadir/doc/%name/transproxy.txt

%changelog
* Mon Jun 02 2025 Nikolay Strelkov <snk@altlinux.org> 3.3-alt1
- Initial build for Sisyphus
