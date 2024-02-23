%define        _unpackaged_files_terminate_build 1

Name:          jruby-launcher
Version:       1.1.19
Release:       alt1
Summary:       JRuby's native launcher executable
License:       CDDL-1.0
Group:         Development/Ruby
Url:           https://github.com/jruby/jruby-launcher
Vcs:           https://github.com/jruby/jruby-launcher.git

Source:        %name-%version.tar
Patch:         %name-%version-%release.patch
BuildRequires: gcc-c++

%description
Maintaning JRuby.BAT was, well, to put it mildly, unpleasant. We had tens of
bugs due to BAT limitations, we had weird behaviors depending on the version
of Windows, we had a bunch of regressions.

%package       -n jruby-native
Summary:       JRuby's native module for ruby
Group:         Development/Ruby

Requires:      jruby-launcher
Requires:      ruby

%description   -n jruby-native
Maintaning JRuby.BAT was, well, to put it mildly, unpleasant. We had tens of
bugs due to BAT limitations, we had weird behaviors depending on the version
of Windows, we had a bunch of regressions.

Native jruby module for ruby.


%prep
%setup
%autopatch -p1

%build
%make

%install
mkdir -p %buildroot%_bindir %buildroot%_libexecdir/ruby/stdlib/rubygems/defaults
%makeinstall_std PREFIX=%buildroot%_prefix
%find_lang %name


%files         -f %name.lang
%doc README.md
%_bindir/*
%_libexecdir/ruby/stdlib/rubygems/defaults/jruby_native.rb


%changelog
* Thu Feb 22 2024 Pavel Skrylev <majioa@altlinux.org> 1.1.19-alt1
- initial build v1.1.19 for Sisyphus
