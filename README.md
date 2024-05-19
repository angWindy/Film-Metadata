# Film-Metadata

![Python](https://img.shields.io/badge/Python-3.12-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Flask-red)
![Frontend](https://img.shields.io/badge/Frontend-HTML/CSS/JS-green)
![API](https://img.shields.io/badge/API-TMDB-fcba03)

# Video demo
https://drive.google.com/file/d/1uPozgeee_IIZx-n3RHwHbDwRfSDciPYy/view?usp=sharing

## Mục đích

Film-Metadata là một dự án Python Framework Frontend API cho việc tìm kiếm thông tin về các bộ phim và diễn viên. Dự án này sử dụng tập dữ liệu Movies Daily Update Dataset để cung cấp thông tin chi tiết về các bộ phim và diễn viên.

## Personas

### Sinh viên:

- **Tên:** Phạm Thị Hồng Nhung
- **Tuổi:** 22
- **Nghề nghiệp:** Sinh viên
- **Mô tả:** Nhung là một sinh viên đại học năm cuối, chuyên ngành Quản trị kinh doanh. Cô ấy thích xem phim để thư giãn và tìm kiếm cảm hứng cho các dự án học tập của mình. Nhung thích các bộ phim tâm lý và lãng mạn, và thường xem phim vào buổi tối sau khi hoàn thành công việc học tập.
- **Nhu cầu:** Nhung cần một công cụ để giúp cô ấy tìm kiếm phim dễ dàng, đề xuất các bộ phim mới dựa trên sở thích của cô ấy, cung cấp thông tin chi tiết về các bộ phim và cho phép cô ấy đánh giá và chia sẻ nhận xét về các bộ phim.
- **Hành vi sử dụng:** Nhung thường sử dụng công cụ tìm kiếm để tìm các bộ phim theo tên hoặc theo thể loại. Cô ấy thích xem các đề xuất phim tương tự sau khi xem một bộ phim. Nhung cũng thích đọc thông tin chi tiết về phim trước khi quyết định xem.
- **Thiết bị sử dụng:** Nhung thường xem phim trên laptop của mình, nhưng cô ấy cũng thích xem phim trên điện thoại di động khi đang di chuyển.

### Giảng viên:

- **Tên:** Nguyễn Văn Minh
- **Tuổi:** 45
- **Nghề nghiệp:** Giảng viên
- **Mô tả:** Minh là một giảng viên đại học với hơn 20 năm kinh nghiệm. Anh ấy thích xem phim để thư giãn và tìm kiếm cảm hứng cho công việc giảng dạy của mình. Minh thích các bộ phim khoa học viễn tưởng và hành động, và thường xem phim vào cuối tuần.
- **Nhu cầu:** Minh cần một công cụ để giúp anh ấy tìm kiếm phim dễ dàng, đề xuất các bộ phim mới dựa trên sở thích của anh ấy, cung cấp thông tin chi tiết về các bộ phim và cho phép anh ấy tạo danh sách phim yêu thích để xem sau.
- **Hành vi sử dụng:** Minh thường sử dụng công cụ tìm kiếm để tìm các bộ phim theo tên hoặc theo diễn viên. Anh ấy thích xem các đề xuất phim tương tự sau khi xem một bộ phim. Minh cũng thích đọc thông tin chi tiết về phim trước khi quyết định xem.
- **Thiết bị sử dụng:** Minh thường xem phim trên máy tính để bàn của mình tại nhà, nhưng anh ấy cũng thích xem phim trên máy tính bảng khi đang nằm trên giường.

## Scenarios: Một số kịch bản cho dự án:

1. **Tìm kiếm phim**:
   - *Người dùng:* Nhung
   - *Mô tả:* Nhung muốn xem một bộ phim tâm lý vào buổi tối. Cô ấy mở ứng dụng và nhập tên phim vào thanh tìm kiếm. Kết quả tìm kiếm hiển thị danh sách các bộ phim phù hợp. Nhung chọn một bộ phim từ danh sách và xem thông tin chi tiết về phim đó.

2. **Đề xuất phim**:
   - *Người dùng:* Minh
   - *Mô tả:* Sau khi xem một bộ phim, Minh muốn xem một bộ phim tương tự. Anh ấy mở ứng dụng và xem các đề xuất phim dựa trên bộ phim anh vừa xem. Minh chọn một bộ phim từ danh sách đề xuất và xem thông tin chi tiết về phim đó.

3. **Đánh giá phim**:
   - *Người dùng:* Nhung
   - *Mô tả:* Sau khi xem một bộ phim, Nhung muốn chia sẻ ý kiến của mình về phim đó. Cô ấy mở ứng dụng, tìm bộ phim cô vừa xem và viết một đánh giá.

4. **Tạo danh sách phim yêu thích**:
   - *Người dùng:* Minh
   - *Mô tả:* Minh muốn tạo một danh sách các bộ phim yêu thích để xem sau. Anh ấy mở ứng dụng, tìm các bộ phim anh muốn xem và thêm chúng vào danh sách yêu thích.

5. **Xem phim trên thiết bị khác nhau**:
   - *Người dùng:* Nhung
   - *Mô tả:* Nhung muốn xem phim trên điện thoại di động của mình khi đang di chuyển. Cô ấy mở ứng dụng trên điện thoại di động, tìm bộ phim cô muốn xem và bắt đầu xem phim.

## User Stories:

**Người dùng:** Alice

### User Story 1: Tìm kiếm phim

**Mô tả:**
Như một người dùng, tôi muốn có khả năng tìm kiếm phim theo tiêu đề hoặc từ khóa liên quan để tìm ra danh sách các phim liên quan.

**Tiêu chí chấp nhận:**
- Tôi có thể nhập tiêu đề phim hoặc từ khóa vào ô tìm kiếm và nhận được kết quả phù hợp.
- Kết quả tìm kiếm hiển thị tiêu đề của các phim liên quan, cùng với hình ảnh minh họa và mô tả ngắn.
- Tôi có thể nhấp vào một phim từ kết quả tìm kiếm để xem thông tin chi tiết về phim đó.

### User Story 2: Xem thông tin chi tiết của một bộ phim

**Mô tả:**
Như một người dùng, sau khi tìm kiếm phim, tôi muốn có khả năng xem thông tin chi tiết về một bộ phim cụ thể để biết thêm về nó.

**Tiêu chí chấp nhận:**
- Tôi có thể nhấp vào một phim từ kết quả tìm kiếm hoặc từ danh sách phim được đề xuất để xem thông tin chi tiết.
- Thông tin chi tiết bao gồm tiêu đề, năm sản xuất, thể loại, đạo diễn, diễn viên chính, mô tả phim, rating, và đánh giá từ người dùng.
- Tôi có thể xem các phim liên quan hoặc các phim mà cùng diễn viên đã tham gia.

### User Story 3: Xem đánh giá và rating của phim

**Mô tả:**
Như một người dùng, tôi muốn có khả năng xem đánh giá và rating của một bộ phim để đánh giá xem liệu nó có phù hợp với sở thích của mình hay không.

**Tiêu chí chấp nhận:**
- Trong thông tin chi tiết của một bộ phim, tôi có thể thấy rating trung bình của phim đó dựa trên đánh giá từ nhiều nguồn khác nhau.
- Tôi có thể đọc các đánh giá từ người dùng trước để hiểu cảm nhận của họ về phim.

### User Story 4: Khám phá các phim liên quan

**Mô tả:**
Như một người dùng, tôi muốn có khả năng khám phá các phim liên quan để mở rộng sở thích điện ảnh của mình.

**Tiêu chí chấp nhận:**
- Trong thông tin chi tiết của một bộ phim, tôi có thể xem danh sách các phim liên quan dựa trên thể loại, đạo diễn hoặc diễn viên.
- Tôi có thể nhấp vào một phim liên quan để xem thông tin chi tiết về phim đó hoặc quay lại danh sách phim để tiếp tục khám phá.


## Tính năng

- Tìm kiếm phim
- Đề xuất tìm kiếm
- Đề xuất các phim tương tự
- Hiển thị thông tin phim (Diễn viên, mô tả, đánh giá,...)

## Cài đặt và cách chạy

1. **Cài Đặt**: Đảm bảo bạn đã cài đặt python>=3.10 trên máy tính của bạn.
2. **Clone Repository**: Clone dự án từ GitHub về máy tính của bạn bằng lệnh sau:

   ```bash
   git clone https://github.com/angWindy/Film-Metadata.git
   ```

3. **Cài đặt và chạy Dự Án**:

   Cài đặt dự án bằng lệnh

   ```bash
   pip install -r requirements.txt   # Đảm bảo rằng bạn đã ở trong thư mục Film-Metadata
   ```

   Khởi động dự án bằng lệnh:

   ```bash
   python main.py
   ```

4. **Truy Cập Ứng Dụng**: Mở trình duyệt và truy cập vào địa chỉ:

   ```
   http://127.0.0.1:5000/
   ```

## Đóng Góp

Chúng tôi rất hoan nghênh mọi đóng góp từ cộng đồng. Nếu bạn muốn đóng góp vào dự án này, vui lòng tạo pull request và chúng tôi sẽ xem xét và hợp nhất nếu phù hợp.

## Tác Giả

- Trần An Thắng - 22022525
- Nguyễn Viết Vũ - 22022632
- Phạm Văn Trường - 22022564

## Tập Dữ liệu

Dự án này sử dụng tập dữ liệu Movies Daily Update Dataset để cung cấp thông tin về các bộ phim và diễn viên. Tập dữ liệu này được cập nhật hàng ngày để đảm bảo thông tin mới nhất về các bộ phim và diễn viên.

[TMDB Movies (900k movies + daily updates)](https://www.kaggle.com/datasets/alanvourch/tmdb-movies-daily-updates)
Film name : TMDB_all_movies.csv

## Tool

[Bootstrap](https://getbootstrap.com/)
