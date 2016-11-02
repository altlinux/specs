Name: mr
Version: 1.20160123
Release: alt1

Summary: A tool to manage all your version control repos
License: GPLv2+
Group: Development/Tools

Url: http://myrepos.branchable.com/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Pavel Nakonechnyi <zorg@altlinux.org>

Provides: mr

BuildArch: noarch
BuildRequires: perl-podlators perl-libwww

%description
The mr(1) command can checkout, update, or perform other actions on
a set of repositories as if they were one combined respository. It
supports any combination of git, svn, mercurial, bzr, darcs, cvs, vcsh,
fossil, and veracity repositories, and support for other version control
systems can easily be added. (There are extensions adding support for unison
and git-svn, among others.)

It is extremely configurable via simple shell scripting. Some examples
of things it can do include:
 * Update a repository no more frequently than once every twelve hours.
 * Run an arbitrary command before committing to a repository.
 * When updating a git repository, pull from two different upstreams
   and merge the two together.
 * Run several repository updates in parallel, greatly speeding up
   the update process.
 * Remember actions that failed due to a laptop being offline, so they
   can be retried when it comes back online.

%package -n mr-webcheckout
Summary: Check out repositories referenced on a web page
Group: Development/Tools
Requires: perl-HTML-Parser

%description -n mr-webcheckout
webcheckout downloads an url and parses it, looking for version control
repositories referenced by the page. It checks out each repository into
a subdirectory of the current directory, using whatever VCS program is
appropriate for that repository (git, svn, etc).

The information about the repositories is embedded in the web page using
the rel=vcs-* microformat, which is documented at
<http://kitenet.net/~joey/rfc/rel-vcs/>.

If the optional destdir parameter is specified, VCS programs will be asked
to check out repositories into that directory. If there are multiple
repositories to check out, each will be checked out into a separate
subdirectory of the destdir.

%prep
%setup
%patch -p1

%build
%make_build

%install
%makeinstall_std
install -d %buildroot%_docdir/%name-%version

%files
%_bindir/mr
%_man1dir/mr*
%_datadir/mr
%doc mrconfig
%doc mrconfig.complex
%doc README

%files -n mr-webcheckout
%_bindir/webcheckout
%_man1dir/webcheckout*

%changelog
* Tue Nov 01 2016 Pavel Nakonechnyi <zorg@altlinux.org> 1.20160123-alt1
- updated to 1.20160123
- mr: create temporary file with '.mrconfig' suffix
- mr: fix config parsing when '-c' and '-d' options are used
- enabled webcheckout subpackage (thx Alexey Borisenkov)
- spec cleanup and update

* Sat Sep 22 2012 Terechkov Evgenii <evg@altlinux.org> 1.13-alt1
- 1.13

* Sat Sep 22 2012 Terechkov Evgenii <evg@altlinux.org> 1.12-alt1
- Initial build for ALT Linux Sisyphus (based on Fedora spec)
