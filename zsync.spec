%global commit 7561a8c81fcd591534c724e6f2d6ea838f4da1bf

Name:           zsync
Version:        0.6.2
Release:        1%{?dist}
Summary:        An rsync-like download optimizer tool

License:        Artistic 2.0
URL:            http://zsync.moria.org.uk
Source0:        https://github.com/cph6/zsync/archive/%{commit}.tar.gz

BuildRequires:  make, gcc, autoconf

Provides:       bundled(zlib) = 1.2.1.1

%description
zsync is a file transfer program. It allows you to download
a file from a remote server, where you have a copy of an
older version of the file on your computer already.

zsync downloads only the new parts of the file. It uses the
same algorithm as rsync. However, where rsync is designed
for synchronising data from one computer to another within
an organisation, zsync is designed for file distribution,
with one file on a server to be distributed to thousands
of downloaders.

zsync requires no special server software â€” just a web server
to host the files â€” and imposes no extra load on the server,
making it ideal for large scale file distribution.


%prep
%autosetup -n zsync-%{commit}


%build
pushd c
    %configure
    %make_build
popd


%install
pushd c
    %make_install
popd

# We'll mark this as license file later
rm -rf %{buildroot}%{_docdir}/zsync/COPYING

%files
%license COPYING
%doc README NEWS
%{_bindir}/zsync*
%{_mandir}/man1/zsync*.1.*


%changelog
* Wed Jan  4 2017 Neal Gompa <ngompa13@gmail.com>
- Initial packaging
