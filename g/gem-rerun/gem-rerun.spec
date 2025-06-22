%define _unpackaged_files_terminate_build 1

%define pkgname rerun

Name: gem-%pkgname
Version: 0.14.0
Release: alt1

Summary: tool to launch commands and restart them on filesystem changes
License: MIT
Group: Development/Ruby
Url: https://github.com/alexch/rerun

BuildArch: noarch

Source: %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
Rerun launches your program, then watches the filesystem. If a relevant
file changes, then it restarts your program. Rerun works for both
long-running processes (e.g. apps) and for short-running ones (e.g.
tests).

Install libnotify-bin to get desktop notifications when your application
is restarted, or about the results of your tests.

%package doc
Summary: Documentation files for %name gem
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir
%_bindir/%pkgname

%files doc
%doc todo.md
%ruby_gemdocdir

%changelog
* Sun Jun 22 2025 Nikolay Strelkov <snk@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
