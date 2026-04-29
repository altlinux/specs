%global _unpackaged_files_terminate_build 1
%define name_orig ruzzy
# Upstream tests require compiled native extensions
# Skipped in RPM build environment
%def_without check

Name: gem-%name_orig
Version: 0.8.0
Release: alt1
Summary: A coverage-guided fuzzer for pure Ruby code and Ruby C extensions
License: AGPL-3.0-only
Group: Development/Ruby
Url: https://github.com/trailofbits/ruzzy
Vcs: https://github.com/trailofbits/ruzzy

Source0: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby
BuildRequires: clang
BuildRequires: libstdc++-devel
BuildRequires: rake
BuildRequires: rake-compiler
%if_with check
BuildRequires: rubocop
BuildRequires: rake-release
%endif

%description
Ruzzy is heavily inspired by Google's Atheris, a Python fuzzer. Like
Atheris, Ruzzy uses libFuzzer for its coverage instrumentation and
fuzzing engine. Ruzzy also supports AddressSanitizer and
UndefinedBehaviorSanitizer when fuzzing C extensions.

%prep
%setup
%autopatch -p1

%build
export CC=/usr/bin/clang
export CXX=/usr/bin/clang++
export LDSHARED="/usr/bin/clang -shared"
export LDSHAREDXX="/usr/bin/clang++ -shared"
export MAKE="%__make --environment-overrides V=1"
%ruby_build

%install
%ruby_install

%check
export GEM_PATH=%_libdir/ruby/gems
ruby -Ilib -e 'require "ruzzy"; puts Ruzzy::VERSION'

%files
%ruby_gemspecdir/%name_orig-%version.gemspec
%ruby_gemslibdir/%name_orig-%version
%ruby_gemsextdir/%name_orig-%version
%ruby_gemsdocdir/%name_orig-%version
%doc LICENSE README.md

%changelog
* Tue Apr 28 2026 Timofei Fedotov <sovtouch@altlinux.org> 0.8.0-alt1
- Updated to 0.8.0.

* Fri Jan 30 2026 Timofei Fedotov <sovtouch@altlinux.org> 0.7.0-alt1
- Initial built for ALT Sisyphus.
