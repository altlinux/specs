# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: rpm-macros-zig
Version: 3
Release: alt1
Summary: RPM macros for Zig
License: GPL-2.0-only
Group: Development/Other
BuildArch: noarch

Source: zig.macros

%description
%summary.

%install
install -pDm644 %SOURCE0 %buildroot%_rpmmacrosdir/zig

%check
set +x
grep -Eo '%%\S+' %SOURCE0 | while read -r m; do
	M=$(rpm \
		--macros='/usr/lib/rpm/macros:%SOURCE0' \
		--define 'name for_buildroot' \
		--eval "$m" </dev/null)
	echo -n "check $m [${#M}] "
	if grep -q '%%' <<<"$M"; then
		echo >&2 "unexpandable [$M]"
		exit 2
	elif [ ${#M} -eq 0 ]; then
		echo "empty"
		exit 3
	else
		echo "ok"
	fi
done

%files
%_rpmmacrosdir/zig

%changelog
* Fri Sep 06 2024 Vitaly Chikunov <vt@altlinux.org> 3-alt1
- Parametrize cache-dir and release/optimize modes.
- spec: Add %%check with basic rpm macros linting.

* Mon Aug 14 2023 Vitaly Chikunov <vt@altlinux.org> 2-alt1
- Update arch list for zig-0.11.0 (remove ppc64le).
- Fix build error: Invalid option: -Drelease-safe.

* Sat Jun 03 2023 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- First version.
