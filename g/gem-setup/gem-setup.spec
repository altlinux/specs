%define        pkgname setup

Name:          gem-%pkgname
Version:       5.999.3
Release:       alt7

Summary:       Ruby's Classic Site Installer
Group:         Development/Ruby
License:       BSD 2-clause Simplified License
Url:           https://github.com/rubyworks/setup
# VCS:         https://github.com/rubyworks/setup.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         patch.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(olddoc)

Requires:      ruby-pry
Requires:      chrpath

%description
Every well practiced Rubyist is aware of Minero Aoki's ever setup.rb script.
It's how most of us used to install our Ruby programs before RubyGems came
along. And it's still mighty useful in certain scenarios, not the least of
which is the job of the distro package maintainer.

Ruby Setup converts setup.rb into a stand-alone application. No longer
requiring the distribution of the setup.rb script with every Ruby package.
Just instruct one's users to install Ruby Setup (gem install setup) and go from
there. As long as a project is setup.rb compliant, as most are, then there is
little to nothing it's developer must do.

%package       doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   doc
Documentation files for %name.

%prep
%setup
%patch -p1

%build
%gem_build --join=lib:bin

%install
%gem_install

%check
%gem_test

%files
%doc README* HISTORY* MANIFEST
%_bindir/*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Tue Apr 30 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt7
- Set default external CP to UTF8

* Tue Apr 23 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt6
- added default value for __dir__ variable, when loading Rakefile info a module,
  this fixes unknown error when adding the var info "$:"
- separated Hoe gemspec detector from the Rakefile one leading to
  correct evaluation of Rakefile in main space
- Now old shebang args in the ruby executables will be passed to new
  shebang line
- Fix sequence so Rakefile will be proceeded before Olddoc gemspecs.
- Rakefile gemspec detector not will not fall when rakefile name is
  nil
! Redone gemspec procedure detection so sequence of gemspecs will be
  affected rather than filelist as before
- Parse olddoc gemspecs before rakefile ones
- Disable adaptive configuration on .so compilation, so extconf.rb will
  be run anytime
+ save aliases also for project and sources
+ add #has_name? to Source::Base to match alises also
+ hot on-source-load gem source version replacement
+ command line for source version replacement called as
  --version-replace
+ added call to chrpath binary to remove RPATH from .so during
  compile action
- Merged detection of the gemfile in hoe or plain rakefile
- Removed hoe/debug module
+ inferring gemfile from Rakefile, so when spec is defined in the
  Rakefile it will be detected
- Fix class name for target ruby from erroneous Site to Ruby
- Fix install folder for i586 arch, so .so files will be installed by
  using x86 arch

* Sat Apr 06 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt5
- fix req deps on executables when they are already installed only
- set autoalias on binaries only for its source not others, and when no
  other source names match the binary

* Tue Apr 02 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt4
- load Gemfile by temporary changing the root when creating the bundler's DSL

* Wed Mar 27 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt3
- fix requires deps detection over executable's shebang line

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt2
- Added novel approach to detect the dependencies of packages

* Sun Mar 17 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt1
- Bump to 5.999.3

* Thu Mar 14 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.2-alt1
- Bump to 5.999.2
- Use Ruby Policy 2.0

* Mon Mar 11 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.1-alt1
- Bump to 5.999.1

* Fri Jan 25 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.0-alt1
- Initial gemified build for Sisyphus with usage Ruby Policy 2.0.
