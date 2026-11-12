%global import_path github.com/writefreely/writefreely
# TODO: some tests require Internet
%def_without check

Name: writefreely
Version: 0.17.3
Release: alt1
Packager: Pavel Nakonechnyi <zorg@altlinux.org>

Summary: Federated blogging from write.as
Group: Networking/WWW
License: AGPL-3.0
Url: https://writefreely.org/

BuildRequires(pre): rpm-macros-golang
BuildRequires(pre): rpm-build-golang
BuildRequires(pre): rpm-macros-systemd
BuildRequires: lessjs go-bindata
BuildRequires: rpm-build-nodejs node node-webpack node-webpack-cli

Source: %name-%version.tar

Source1: vendor.tar

Source2: %name.service
Source3: %name.tmpfiles
Source4: config.ini
Source5: nginx_writefreely.conf

Source6: prose.tar

%description
WriteFreely is free and open source software for easily publishing writing on
the web. Built on a plain, auto-saving editor, WriteFreely gives you a
distraction-free writing environment. Once published, your words are front and
center, and easy to read.

%package nginx
Summary: nginx web-server default configuration for %name
Group: Networking/WWW
BuildArch: noarch
Requires: %name = %EVR nginx
Requires(post): cert-sh-functions

%description nginx
nginx web-server default configuration for %name.

%prep
%setup -a1
%setup -DTa6

%build
pushd less
# TODO: less clean-css plugin is required to compile CSS with --clean-css="--s1 --advanced" flag
CSSDIR=../static/css
lessc app.less ${CSSDIR}/write.css
lessc fonts.less ${CSSDIR}/fonts.css
lessc icons.less ${CSSDIR}/icons.css
lessc prose.less ${CSSDIR}/prose.css
popd

pushd prose
NODE_OPTIONS=--openssl-legacy-provider npm run-script build
popd

#go build -v -tags='sqlite' ./cmd/writefreely
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export TAGS="sqlite"
export LDFLAGS="-X 'github.com/writeas/writefreely.softwareVer=%version-%release'"
%golang_prepare

pushd .build/src/%import_path
%golang_build ./cmd/writefreely
popd

%check
cd .build/src/%import_path
go test -v ./...

%install
install -dm755 %buildroot%_datadir/%name/pages
install -dm755 %buildroot%_datadir/%name/static
install -dm755 %buildroot%_datadir/%name/templates

install -pD -m644 %SOURCE2 -t %buildroot/%_unitdir/
install -pD -m644 %SOURCE3 %buildroot/%_tmpfilesdir/%name.conf
install -pD -m644 %SOURCE4 %buildroot/%_sysconfdir/%name/config.ini
install -pD -m755 .build/bin/writefreely %buildroot/%_bindir/%name

cp -rp pages/* %buildroot%_datadir/%name/pages
cp -rp static/* %buildroot%_datadir/%name/static
cp -rp templates/* %buildroot%_datadir/%name/templates

mkdir -p %buildroot%_localstatedir/%name/data
mkdir -p %buildroot%_localstatedir/%name/keys

install -pD -m0644 %SOURCE5 %buildroot%_sysconfdir/nginx/sites-available.d/%name.conf

%pre
/usr/sbin/groupadd -r -f _writefreely 2>/dev/null ||:
/usr/sbin/useradd -r -g _writefreely -d / -s /dev/null -N -c "WriteFreely" _writefreely >/dev/null 2>&1 ||:

%post nginx
# Generate SSL key
. cert-sh-functions
ssl_generate "writefreely"

%files
%_bindir/%name
%_datadir/%name
%dir %attr(0700,_writefreely,_writefreely) %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config.ini
%dir %attr(0700,_writefreely,_writefreely) %_localstatedir/%name
%_unitdir/%name.service
%_tmpfilesdir/%name.conf

%files nginx
%config(noreplace) %attr(0644,root,root) %_sysconfdir/nginx/sites-available.d/%name.conf

%post
echo "writefreely: for database migration see https://blog.writefreely.org/tag:release, 'sudo /usr/bin/writefreely -c /etc/writefreely/config.ini db migrate'"
%post_systemd_postponed writefreely

%preun
%preun_systemd writefreely

%changelog
* Thu Nov 12 2026 Pavel Nakonechnyi <zorg@altlinux.org> 0.17.3-alt1
- version 0.17.3
- fixes:
  + GHSA-7jv7-gf23-wcqq: authentication bypass via API access tokens
  + GHSA-cx5r-gg25-76ph: private and password-protected blog content exposed via the ActivityPub outbox
  + GHSA-wvrr-gx9p-xvxm: server-side request forgery (SSRF) via WebFinger lookups
  + GHSA-7635-vx4w-qww7: unauthenticated SSRF via ActivityPub inbox actor / object resolution
  + GHSA-22qx-x758-m72p: IPv6 transition address bypass of SSRF protections in federation
  + GHSA-mp2f-3fq8-r9vj: add CSRF protection to account settings endpoints (/me and /api/me)
  + GHSA-g4m9-5p4q-ch24: Enforce the maximum blogs per user limit when creating blogs via the API
  + GHSA-7mmq-gh5f-97p3: Prevent users from changing settings on another user's blog via the API
  + GHSA-wqc7-9ph9-m5fm: Prevent users from changing metadata on blogs they don't own
  + GHSA-cwxm-8ch5-j2vh: stored XSS via unsanitized post slugs in RSS, email, and ActivityPub output
  + GHSA-hwfg-mg9c-cvgf: Prevent users from pinning or unpinning other users' posts
  + UNASSIGNED: Enforce signup checks consistently across all registration paths, extending the invite code validation from v0.17.2 to API and OAuth signups

* Mon Aug 10 2026 Pavel Nakonechnyi <zorg@altlinux.org> 0.17.2-alt1
- version 0.17.2
- Fixes:
+ UNASSIGNED: Registration bug not fully fixed

* Sun Aug 02 2026 Pavel Nakonechnyi <zorg@altlinux.org> 0.17.1-alt1
- version 0.17.1

* Sat Jul 18 2026 Pavel Nakonechnyi <zorg@altlinux.org> 0.17.0-alt1
- version 0.17.0
- Fixes:
+ CVE-2025-24337: Fix config.ini defaults to world-readable
+ GHSA-cfcq-76gr-62x8: Fix Cross-User IDOR: Subscriber List Disclosure
+ UNASSIGNED: Prevent signups via /auth/signup with closed registrations

* Sat Nov 23 2024 Pavel Nakonechnyi <zorg@altlinux.org> 0.15.1-alt1
- version 0.15.1

* Sat May 18 2024 Pavel Nakonechnyi <zorg@altlinux.org> 0.15.0-alt2
- remove sqlite build dependency (closes #50379)

* Sun May 05 2024 Pavel Nakonechnyi <zorg@altlinux.org> 0.15.0-alt1
- version 0.15.0

* Mon May 29 2023 Pavel Nakonechnyi <zorg@altlinux.org> 0.13.2-alt1
- version 0.13.2
- update build process to handle vendoring manually

* Mon Dec 13 2021 Pavel Nakonechnyi <zorg@altlinux.org> 0.13.1-alt1
- initial build
