%define _unpackaged_files_terminate_build 1

Name: gem-afl-ruby
Version: 0.0.3
Release: alt1.cbaad7a

Summary: AFL for Ruby
Group: Development/Ruby
License: MIT
URL: https://github.com/richo/afl-ruby.git
VCS: https://github.com/richo/afl-ruby.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-ruby
BuildRequires: rpm-build-ruby

%description
AFL for Ruby.

%package doc
Group: Development/Documentation
Summary: Documentation for afl-ruby

%description doc
Documentation for afl-ruby.

%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspecdir/afl-%version.gemspec
%ruby_gemslibdir/afl-%version
%ruby_gemsextdir/afl-%version

%files doc
%doc README.md
%ruby_gemsdocdir/afl-%version

%changelog
* Mon Feb 02 2026 Ilya Muhamadeev <nicourced@altlinux.org> 0.0.3-alt1.cbaad7a
- Initial build.

