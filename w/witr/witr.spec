%define _unpackaged_files_terminate_build 1

Name: witr
Version: 0.3.3
Release: alt1

Summary: Why is this running?
License: Apache-2.0
Group: Monitoring
Url: https://github.com/pranshuparmar/witr

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang

BuildRequires: golang

%description
witr exists to answer a single question: "Why is this running?".

When something is running on a system - whether it is a process,
a service, or something bound to a port - there is always a cause.
That cause is often indirect, non-obvious, or spread across multiple
layers such as supervisors, containers, services, or shells.

Existing tools (ps, top, lsof, ss, systemctl, docker ps) expose state
and metadata. They show what is running, but leave the user to infer
why by manually correlating outputs across tools.

witr makes that causality explicit.

It explains where a running thing came from, how it was started, and
what chain of systems is responsible for it existing right now,
in a single, human-readable output.

%prep
%setup

%build
go build -ldflags "-X main.version=v%{version}" -o witr ./cmd/witr

%install
install -Dm 0755 witr %buildroot%_bindir/witr
install -Dm 644 docs/cli/witr.1 %buildroot%_man1dir/witr.1

%files
%doc LICENSE README.md
%_bindir/witr
%_man1dir/witr.1.*

%changelog
* Fri Jun 26 2026 Nikolay Strelkov <snk@altlinux.org> 0.3.3-alt1
- New version 0.3.3.

* Sun May 17 2026 Nikolay Strelkov <snk@altlinux.org> 0.3.2-alt1
- New version 0.3.2.

* Fri Mar 20 2026 Nikolay Strelkov <snk@altlinux.org> 0.3.1-alt1
- New version 0.3.1.

* Sun Feb 22 2026 Nikolay Strelkov <snk@altlinux.org> 0.3.0-alt1
- New version 0.3.0.

* Fri Feb 13 2026 Nikolay Strelkov <snk@altlinux.org> 0.2.7-alt1
- New version 0.2.7.

* Thu Jan 22 2026 Nikolay Strelkov <snk@altlinux.org> 0.2.6-alt1
- New version 0.2.6.

* Sun Jan 18 2026 Nikolay Strelkov <snk@altlinux.org> 0.2.5-alt1
- New version 0.2.5.

* Thu Jan 15 2026 Nikolay Strelkov <snk@altlinux.org> 0.2.4-alt1
- New version 0.2.4.

* Sun Jan 11 2026 Nikolay Strelkov <snk@altlinux.org> 0.2.3-alt1
- New version 0.2.3.

* Thu Jan 08 2026 Nikolay Strelkov <snk@altlinux.org> 0.2.1-alt1
- New version 0.2.1.

* Wed Jan 07 2026 Nikolay Strelkov <snk@altlinux.org> 0.1.8-alt1
- New version 0.1.8.

* Fri Jan 02 2026 Nikolay Strelkov <snk@altlinux.org> 0.1.6-alt1
- New version 0.1.6.

* Thu Jan 01 2026 Nikolay Strelkov <snk@altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus
