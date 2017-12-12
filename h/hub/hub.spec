%define gobuild go build

# TODO: build with external sources

Name: hub
Version: 2.2.9
Release: alt1

Summary: A command-line wrapper for git with github shortcuts

Group: Development/Tools
License: MIT
Url: http://hub.github.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/github/hub/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-golang
ExclusiveArch: %go_arches

BuildRequires: golang >= 1.7

BuildRequires: git-core

#BuildRequires: golang(gopkg.in/yaml.v1)
#BuildRequires: golang(github.com/bmizerany/assert)
#BuildRequires: golang(github.com/BurntSushi/toml)
#BuildRequires: golang(github.com/howeyc/gopass)
#BuildRequires: golang(github.com/kballard/go-shellquote)
#BuildRequires: golang(github.com/mitchellh/go-homedir)

Requires: git-core

#Provides: bundled(golang(github.com/inconshreveable/go-update))
#Provides: bundled(golang(github.com/mattn/go-colorable))
#Provides: bundled(golang(github.com/mattn/go-isatty))
#Provides: bundled(golang(github.com/octokit/go-octokit))
#Provides: bundled(golang(github.com/ogier/pflag))

%description
hub is a command line tool that wraps `git` in order to extend it with extra
features and commands that make working with GitHub easier.

    $ hub clone rtomayko/tilt

    # expands to:
    $ git clone git://github.com/rtomayko/tilt.git

%prep
%setup

#rm -rf vendor/gopkg.in/yaml.v1 \
#       vendor/github.com/bmizerany/assert \
#       vendor/github.com/BurntSushi/toml \
#       vendor/github.com/howeyc/gopass \
#       vendor/github.com/kballard/go-shellquote \
#       vendor/github.com/mitchellh/go-homedir

# TODO: macro
mkdir -p Godeps/src/github.com/github
ln -snf $(pwd) Godeps/src/github.com/github/hub

%build
export GOPATH=$(pwd):$(pwd)/Godeps:%go_path
%gobuild -o bin/%name -ldflags '-X github.com/github/hub/version.Version=2.2.9'

%install
# /bin/hub
install -D -p -m 755 bin/%name %buildroot%_bindir/%name

# Documentation
install -d -m 755 %buildroot%_man1dir/
cp -p man/hub.1 %buildroot%_man1dir/.

# Bash-completion
install -d -m 755 %buildroot%_sysconfdir/bash_completion.d/
cp -p etc/hub.bash_completion.sh %buildroot%_sysconfdir/bash_completion.d/.

# ZSH-completion
install -d -m 755 %buildroot%_datadir/zsh/site-functions/
cp -p etc/hub.zsh_completion %buildroot%_datadir/zsh/site-functions/_hub

%check

%if_with tests
# Tests are currently nonfunctional in mock
# All calls to 'git' are failing to find a valid repo, but
# they work when run outside of mock.

export GOPATH=$(pwd):$(pwd)/Godeps:%gopath

find . -maxdepth 2 -name '*.go' '!' -name '*_test.go' | \
  cut -d/ -f2 | sort -u | grep -v '.go$' | sed 's!^!github.com/github/hub/!' | \
  xargs go test -v
%endif

%files
%doc LICENSE
%doc README.md CONTRIBUTING.md
%doc man/hub.1.html man/hub.1.ronn
%_bindir/hub
%_man1dir/hub.1.*
%_sysconfdir/bash_completion.d/
%_datadir/zsh/site-functions/_hub

%changelog
* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 2.2.9-alt1
- initial build for ALT Sisyphus

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Stephen Gallagher <sgallagh@redhat.com> - 2.2.9-3
- Rebuild for golang bug that caused segfaults

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 17 2016 Stephen Gallagher <sgallagh@redhat.com> - 2.2.9-1
- Update to latest stable release 2.2.9

* Wed Sep 28 2016 Stephen Gallagher <sgallagh@redhat.com> - 2.2.5-3
- Really fix location of ZSH completion script

* Tue Sep 13 2016 Stephen Gallagher <sgallagh@redhat.com> - 2.2.5-2
- Fix location of ZSH completion script

* Wed Aug 31 2016 Stephen Gallagher <sgallagh@redhat.com> - 2.2.5-1
- Update to new (and latest) major release of hub
- Include ZSH completion script

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Ralph Bean <rbean@redhat.com> - 1.12.4-5
- Adjust ownership of bash_completion file/dir.

* Fri Sep 11 2015 Ralph Bean <rbean@redhat.com> - 1.12.4-4
- Ship bash completion file.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Ralph Bean <rbean@redhat.com> - 1.12.4-2
- Require ruby (for ruby-mri.  jruby and hub don't get along.)
  https://bugzilla.redhat.com/show_bug.cgi?id=1225254

* Wed Apr 22 2015 Ralph Bean <rbean@redhat.com> - 1.12.4-1
- New version
- Stop building with rdoc for now because its being so squirrely.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Ralph Bean <rbean@redhat.com> - 1.12.1-1
- Latest upstream.

* Thu May 22 2014 Ralph Bean <rbean@redhat.com> - 1.12.0-4
- Add -doc subpackage with rdoc product.
- Add check section, but left it commented out due to dep issues.
- Remove spurious man files.
- Remove weirdly nested docs from rdoc.

* Wed Apr 02 2014 Ralph Bean <rbean@redhat.com> - 1.12.0-3
- Update Source0 URL to use the github guidelines.
- Replace weird %%prep %%setup stuff with something more familiar.

* Wed Apr 02 2014 Ralph Bean <rbean@redhat.com> - 1.12.0-2
- Remove version from the doc directory.
- Replace install macro with just "install".

* Mon Mar 31 2014 Ralph Bean <rbean@redhat.com> - 1.12.0-1
- Initial packaging for Fedora
