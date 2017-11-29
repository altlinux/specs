%def_disable debug

%define gitdate 20111225
Name: rebar
Version: 2.git%gitdate
Release: alt1.1
Summary: A sophisticated build-tool for Erlang projects that follows OTP principles.
License: %asl
Group: Development/Erlang
URL: https://github.com/basho/rebar
Source: %name-%version.tar
Patch0: %name-add-ignore-cmd-list.patch
Patch1: %name-default-jobs-1.patch
Patch2: %name-add_patha.patch
BuildArch: noarch
Requires: erlang-otp erlang-visual erlang-common_test
Packager: Sergey Shilov <hsv@altlinux.org>

BuildRequires(pre): rpm-build-erlang rpm-build-licenses
BuildRequires: erlang-devel erlang-otp-devel erlang-visual-devel erlang-common_test-devel

%description
rebar is an Erlang build tool that makes it easy to compile and
test Erlang applications, port drivers and releases.

rebar is a self-contained Erlang script, so it's easy to distribute or even
embed directly in a project. Where possible, rebar uses standard Erlang/OTP
conventions for project structures, thus minimizing the amount of build
configuration work. rebar also provides dependency management, enabling
application writers to easily re-use common libraries from a variety of
locations (git, hg, etc).


%prep
%setup -n  %name-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1


%build
./bootstrap

%install
%__mkdir_p %buildroot/%_bindir
%__install -m755 rebar %buildroot/%_bindir


%files
%_bindir/*


%changelog
* Mon Oct 23 2017 Denis Medvedev <nbr@altlinux.org> 2.git20111225-alt1.1
- just a rebuild for OTP 19.

* Tue Dec 27 2011 Sergey Shilov <hsv@altlinux.org> 2.git20111225-alt1
- 2.git20111225:
  + Erlang R15B support
  + Fix rebar_core crash
  + Fix help text formatting
  + Fix and refactor reltool root_dir lookup
  + Universally support apps=/skip_apps=
  + Add support for arch-specific hooks
  + Add support for first_files to port compiler
  + Add root_dir option to reltool.config
  + Add support for -p flag to profile rebar run
  + Add -D support to rebar_port_compiler
  + Add possibility to make symbolic links
  + Support for custom version commands
  + Load plugins dynamically from source


* Tue Aug 02 2011 Sergey Shilov <hsv@altlinux.org> 2.git20110801-alt1
- 2.git20110801:
  + Fix error handling bug in {copy,In,Out} template
  + Fix grep portability
  + Fix {git,Url} support
  + fix erlexec parameter
  + Fix logging
  + Fix erlc regression
  + Fix leftover whitespace errors
  + Fix indentation errors
  + Fix code readability in port_compiler
  + Fix eunit regression (reported-by Alexander Dorofeev)
  + Skip appup generation for new app in release
  + Extend port compiler default env for Darwin 11 32-bit
  + Restore R13B03 compatibility for building rebar
  + The ability to overload macros was added in Erlang R13B04.
  + Adapt basicnif template to OTP changes
  + Optimize list ops and error reporting in sh/2
  + Sync rel/files in dummy project with templates
  + Change shebang lines to /bin/sh
  + Allow plugins to run before/after a rebar command.
  + Make port compilation template configurable
  + Recursively search "src" for .proto files
  + Add support for {copy, src, dst} to templater
  + Add support for $HOME/.rebar/config
  + Add support for command-specific env for hooks
  + Add list-deps command
  + Add file local variables where appropriate


* Thu Apr 14 2011 Sergey Shilov <hsv@altlinux.org> 2.git20110411-alt1
Initial build.

